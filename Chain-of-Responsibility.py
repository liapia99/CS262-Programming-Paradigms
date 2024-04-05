from abc import ABC, abstractmethod

class AccessHandler(ABC):
    @abstractmethod
    def handle_request(self, user):
        pass

class BasicAccessHandler(AccessHandler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, user):
        if user.role == "basic":
            print("Basic access granted.")
        elif self.successor:
            self.successor.handle_request(user)
        else:
            print("Access denied.")

class PremiumAccessHandler(AccessHandler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, user):
        if user.role == "premium":
            print("Premium access granted.")
        elif self.successor:
            self.successor.handle_request(user)
        else:
            print("Access denied.")

class User:
    def __init__(self, role):
        self.role = role

class OrderingSystem:
    def __init__(self):
        self.success_handler = BasicAccessHandler(PremiumAccessHandler())
    def process_order(self, user):
        print("Processing order...")
        self.success_handler.handle_request(user)

def main():
    ordering_system = OrderingSystem()

    user1 = User("basic")
    user2 = User("premium")
    user3 = User("none")

    ordering_system.process_order(user1)
    ordering_system.process_order(user2)
    ordering_system.process_order(user3)

if __name__=="__main__":
    main()
