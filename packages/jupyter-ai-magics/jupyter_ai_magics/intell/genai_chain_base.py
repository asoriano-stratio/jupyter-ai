from abc import abstractmethod, ABC


class BaseStratioGenAIChain(ABC):

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def process_prompt(self, prompt) -> str:
        pass
