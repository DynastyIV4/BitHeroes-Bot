from abc import ABC, abstractmethod

class Subscriber(ABC):

    @abstractmethod
    def update():
        pass

class Publisher(ABC):
    
    def __init__(self):
        self.subscribers: list[Subscriber] = []   
    
    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
    
    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()

