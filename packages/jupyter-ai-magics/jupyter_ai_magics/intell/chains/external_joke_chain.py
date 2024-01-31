import os
import requests
from jupyter_ai_magics.intell.genai_chain_base import BaseStratioGenAIChain


class JokeStratioGenAIChain(BaseStratioGenAIChain):

    def __init__(self, *args, **kwargs):
        super(JokeStratioGenAIChain, self).__init__(*args, **kwargs)
        self.genai_server_url = os.environ.get("INTELL_GENAI_STRATIO_GENAI_SERVICE_URL", "http://127.0.0.1:8081/")
        self.genai_server_endpoint = "/v1/chains/chain_joke/invoke"

    def process_prompt(self, prompt):

        response = requests.post(
            url=f"{self.genai_server_url}{self.genai_server_endpoint}",
            headers={"Accept": f"application/json"},
            json={
                "input": {
                    "topic": prompt
                }
            }
        )
        if response.status_code == 200:
            data = response.json()
            answer = data["output"]["content"]
            return answer
        else:
            answer = f"Status code: {response.status_code} Response: {response.json()}"
            return answer
