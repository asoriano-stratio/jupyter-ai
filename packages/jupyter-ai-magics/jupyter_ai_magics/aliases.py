

MODEL_ID_ALIASES = {
    "gpt2": "huggingface_hub:gpt2",
    "gpt3": "openai:text-davinci-003",
    "chatgpt": "openai-chat:gpt-3.5-turbo",
    "gpt4": "openai-chat:gpt-4",
    "ernie-bot": "qianfan:ERNIE-Bot",
    "ernie-bot-4": "qianfan:ERNIE-Bot-4",
    "titan": "bedrock:amazon.titan-tg1-large",
}

from jupyter_ai_magics.intell.chains.external_joke_chain import JokeStratioGenAIChain

INTELL_MODEL_ID_ALIASES = {
    "stratio_genai": "stratio_genai_provider:*",
    "joke": JokeStratioGenAIChain()
}
