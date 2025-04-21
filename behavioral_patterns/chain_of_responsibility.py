from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    Abstract Handler class that defines the interface for handling requests.
    Each concrete handler should implement the `handle` method.
    """
    def __init__(self, successor: Optional[Handler] = None) -> None:
        self.successor = successor

    @abstractmethod
    def handle(self, request: Any) -> str:
        """
        Handle the request. If the handler can process the request, it should return a response.
        Otherwise, it should pass the request to the next handler in the chain.
        """
        pass
    def set_successor(self, successor: Handler) -> None:
        """
        Set the next handler in the chain.
        """
        self.successor = successor
    def next_handler(self, request: Any) -> str:
        """
        Pass the request to the next handler in the chain if it exists.
        """
        if self.successor:
            return self.successor.handle(request)
        return "No handler found for the request."
class ConcreteHandlerA(Handler):
    """
    Concrete Handler A that processes requests of type A.
    """
    def handle(self, request: Any) -> str:
        if request == "A":
            return "ConcreteHandlerA handled the request."
        else:
            return self.next_handler(request)
class ConcreteHandlerB(Handler):
    """
    Concrete Handler B that processes requests of type B.
    """
    def handle(self, request: Any) -> str:
        if request == "B":
            return "ConcreteHandlerB handled the request."
        else:
            return self.next_handler(request)
class ConcreteHandlerC(Handler):
    """
    Concrete Handler C that processes requests of type C.
    """
    def handle(self, request: Any) -> str:
        if request == "C":
            return "ConcreteHandlerC handled the request."
        else:
            return self.next_handler(request)
class Client:
    """
    Client class that creates the chain of handlers and sends requests to the chain.
    """
    def __init__(self) -> None:
        self.handler_chain = self.create_chain()

    def create_chain(self) -> Handler:
        """
        Create the chain of handlers.
        """
        handler_a = ConcreteHandlerA()
        handler_b = ConcreteHandlerB()
        handler_c = ConcreteHandlerC()

        handler_a.set_successor(handler_b)
        handler_b.set_successor(handler_c)

        return handler_a

    def send_request(self, request: Any) -> str:
        """
        Send a request to the chain of handlers.
        """
        return self.handler_chain.handle(request)
# Example usage
if __name__ == "__main__":
    client = Client()
    print(client.send_request("A"))  # Output: ConcreteHandlerA handled the request.
    print(client.send_request("B"))  # Output: ConcreteHandlerB handled the request.
    print(client.send_request("C"))  # Output: ConcreteHandlerC handled the request.
    print(client.send_request("D"))  # Output: No handler found for the request.
    print(client.send_request("A"))  # Output: ConcreteHandlerA handled the request.
    print(client.send_request("B"))  # Output: ConcreteHandlerB handled the request.
    print(client.send_request("C"))  # Output: ConcreteHandlerC handled the request.
    print(client.send_request("D"))  # Output: No handler found for the request.
    print(client.send_request("A"))  # Output: ConcreteHandlerA handled the request.
    print(client.send_request("B"))  # Output: ConcreteHandlerB handled the request.
    print(client.send_request("C"))  # Output: ConcreteHandlerC handled the request.
    print(client.send_request("D"))  # Output: No handler found for the request.
    print(client.send_request("A"))  # Output: ConcreteHandlerA handled the request.
    print(client.send_request("B"))  # Output: ConcreteHandlerB handled the request.