from typing import (
    Any,
    Coroutine,
)

from jupyter_ai_magics import BaseProvider
from jupyter_ai_magics.providers import TextField
from langchain.schema import LLMResult

from .llm import StratioChatService


class StratioGenAIProvider(BaseProvider, StratioChatService):
    id = "stratio_genai_provider"
    name = "Stratio GenAI provider"

    """Kwarg expected by the upstream LangChain provider."""
    model_id_key = "model"

    """List of supported models by their IDs. For registry providers, this will be just ["*"]."""
    models = ["*"]
    help = "Stratio GenAI Service: acts as a gateway to final LLM provider"

    """
    Settings in chat configuration interface:
        User inputs expected by this provider when initializing it.
    """
    fields = [
        TextField(key="stratio_genai_service_url",
                  label="Stratio GenAI Service URL",
                  format="text"
                  ),
        TextField(key="intell_genai_chat_manager",
                  label="Chat manager (optional): intelligence (default) | stratio_genai",
                  format="text"
                  )
    ]

    def __init__(self, **kwargs):
        # print(f"Init StratioAIProvider: kwargs={kwargs}")
        # kwargs["initial_response_line"] = "Test - Custom provider: paso de propiedades a custom LangChain LLM"
        super().__init__(**kwargs)

    @property
    def allows_concurrency(self):
        """
        Nota: se usa en el método de generar notebook
        """
        return True

    async def _acall(self, *args, **kwargs) -> Coroutine[Any, Any, str]:
        """
        Nota: Pisar el método _acall para hacerlo asincrono usando un thread

        Calls self._call() asynchronously in a separate thread for providers
        without an async implementation. Requires the event loop to be running.
        """
        return await self._call_in_executor(*args, **kwargs)

    async def _agenerate(self, *args, **kwargs) -> Coroutine[Any, Any, LLMResult]:
        """
        Calls self._generate() asynchronously in a separate thread for providers
        without an async implementation. Requires the event loop to be running.
        """
        return await self._generate_in_executor(*args, **kwargs)


