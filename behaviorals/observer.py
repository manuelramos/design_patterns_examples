from typing import Protocol


class ISubscriber(Protocol):
    def update(self, message: str) -> None:
        ...


class IPublisher(Protocol):
    def register_subscriber(self, subscriber: ISubscriber) -> None:
        ...

    def unregister_subscriber(self, subscriber: ISubscriber) -> None:
        ...

    def notify_subscribers(self, message: str) -> None:
        ...


class Subscriber(ISubscriber):
    def __init__(self, name:str) -> None:
        self._name = name

    def update(self, message: str) -> None:
        print(f"{self._name} got message '{message}'")

class Publisher(IPublisher):
    def __init__(self) -> None:
        self._subscribers = set()

    def register_subscriber(self, subscriber: ISubscriber) -> None:
        self._subscribers.add(subscriber)

    def unregister_subscriber(self, subscriber: ISubscriber) -> None:
        self._subscribers.remove(subscriber)

    def notify_subscribers(self, message: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(message)


if __name__ == "__main__":
    publisher = Publisher()
    subscriber1 = Subscriber("John")
    subscriber2 = Subscriber("Mary")

    publisher.register_subscriber(subscriber1)
    publisher.register_subscriber(subscriber2)
    publisher.notify_subscribers("Hello World")
    
    publisher.unregister_subscriber(subscriber1)
    publisher.notify_subscribers("Hello World Again")
