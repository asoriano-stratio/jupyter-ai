from jupyter_ai.chat_handlers.base import BaseChatHandler, SlashCommandRoutingType
from jupyter_ai.models import HumanChatMessage
from jupyter_ai_magics.intell.chains.external_joke_chain import JokeStratioGenAIChain

from jupyter_ai_magics.intell.utils import mixedomatic


@mixedomatic
class JokeChatHandler(BaseChatHandler, JokeStratioGenAIChain):
    id = "joke"
    name = "Joke"
    help = "A chat handler that interact with Stratio GenAI Joke chain"
    routing_type = SlashCommandRoutingType(slash_id="joke")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def process_message(self, message: HumanChatMessage):
        prompt = " ".join(message.body.split(" ")[1:])
        response = self.process_prompt(prompt)
        self.reply(response=response, human_msg=message)
