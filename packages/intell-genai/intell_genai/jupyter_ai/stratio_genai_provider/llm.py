from __future__ import annotations

from typing import Any, Dict, Union
from typing import List, Mapping, Optional

import requests
from langchain.adapters.openai import convert_message_to_dict, convert_dict_to_message
from langchain.callbacks.manager import (
    CallbackManagerForLLMRun,
)
from langchain.utils import get_from_dict_or_env
from langchain_community.adapters.openai import convert_openai_messages
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage
from langchain_core.outputs import ChatGeneration
from langchain_core.outputs import ChatResult
from langchain_core.pydantic_v1 import BaseModel, root_validator


# TODO - Cambiar nombre - se usa también en notebook
class StratioChatService(BaseChatModel):
    stratio_genai_service_url: str = ""
    intell_genai_chat_manager: str = ""

    @property
    def _llm_type(self) -> str:
        return "stratio-chat-llm-service"

    # @property
    # def _identifying_params(self) -> Mapping[str, Any]:
    #     """Get the identifying parameters."""
    #     return {
    #         "initial_response_line": self.initial_response_line
    #     }

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        values["stratio_genai_service_url"] = get_from_dict_or_env(
            data=values,
            key="stratio_genai_service_url",
            env_key="INTELL_GENAI_STRATIO_GENAI_SERVICE_URL"
        )
        values["intell_genai_chat_manager"] = get_from_dict_or_env(
            data=values,
            key="intell_genai_chat_manager",
            env_key="INTELL_GENAI_CHAT_MANAGER",
            default="intelligence"
        )
        return values

    def request_stratio_genai_service(self, endpoint: str, payback: dict):
        response = requests.post(
            url=f"{self.stratio_genai_service_url}{endpoint}",
            headers={"Accept": f"application/json"},
            json=payback
        )

        if response.status_code != 200:
            optional_detail = response.json().get("error")
            raise ValueError(
                f"Failed with status code {response.status_code}."
                f" Details: {optional_detail}"
            )
        full_response = response.json()

        return full_response

    def _generate(self,
                  messages: List[BaseMessage],
                  stop: Optional[List[str]] = None,
                  run_manager: Optional[CallbackManagerForLLMRun] = None,
                  **kwargs: Any
                  ) -> ChatResult:

        # => Note: Chat manager
        #     · intelligence:  ConversationChain lives in Analytic
        #                         Array[messages]    -->  Stratio GenAI ( ProxyChain == intell_chat )        --> OpenAI
        #     · stratio_genai: ConversationChain lives in Stratio GenAI
        #                         Last human message -->  Stratio GenAI ( ConvChain == genai_intell_chat ) --> OpenAI

        if self.intell_genai_chat_manager == "intelligence":
            service_endpoint = "/v1/chains/intell_chat/invoke"

            # List[BaseMessage] => server payload
            messages_dicts = [convert_message_to_dict(m) for m in messages]
            payload = {
                "input": {
                    "conversation": {
                        "messages": messages_dicts
                    }
                }
            }

            stratio_genai_response = self.request_stratio_genai_service(service_endpoint, payload)

            chat_result: ChatResult = self._create_chat_result(stratio_genai_response, response_prop="content")

            return chat_result

        else:
            service_endpoint = "/v1/chains/genai_intell_chat/invoke"

            # Getting last Human message
            human_msg = messages[-1]
            payload = {
                "input": {
                    "input": human_msg.content
                }
            }

            stratio_genai_response = self.request_stratio_genai_service(service_endpoint, payload)

            chat_result: ChatResult = self._create_chat_result(stratio_genai_response, response_prop="response")

            return chat_result


    def _create_chat_result(self, response: Union[dict, BaseModel], response_prop = "content") -> ChatResult:
        generations = []
        if not isinstance(response, dict):
            response = response.dict()
        content = response['output'][response_prop]
        message = AIMessage(content=content)
        gen = ChatGeneration(message=message)
        generations.append(gen)

        return ChatResult(generations=generations, llm_output=response)
