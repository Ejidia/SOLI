#OCP CODE
# Importing tools to support abstract classes and methods
from abc import ABC, abstractmethod

# This is an abstract base class named 'Payment'.
# It defines a generic blueprint for all payment types.
# Applying the Open/Closed Principle: the base class doesn't change,
# but new payment types can extend it.
class Payment(ABC):

    # Abstract method that must be implemented by any subclass.
    # It enforces that all payment types must define their own 'process' behavior.
    @abstractmethod
    def process(self):
        pass

# This class represents payment made via credit card.
# It extends the base 'Payment' class and provides a concrete implementation of 'process'.
class CreditCardPayment(Payment):
    
    # The specific logic for handling credit card payments.
    def process(self):
        print("Processing credit card payment")

# This class represents payment made via mobile money.
# It also extends 'Payment' and has its own version of the 'process' method.
class MobileMoneyPayment(Payment):
    
    # The specific logic for handling mobile money payments.
    def process(self):
        print("Processing mobile money payment")

# This function takes any object that implements the 'Payment' interface.
# It calls the 'process' method without needing to know the specific type of payment.
# This makes the function flexible and extensible—perfect for OCP.
def handle_payment(payment: Payment):
    payment.process()

    # In conclusion,The Payment class is closed for modification: we don’t change its internal code.
    #The system is open for extension: we can add BankTransferPayment or any other payment.
    # without touching existing classes or logic in handle_payment.
    #