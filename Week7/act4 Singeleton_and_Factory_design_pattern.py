"""
Design Explanation:

This program uses two design patterns: Factory and Singleton.

The Factory Pattern helps create different payment method objects based on a string input, 
such as "paypal" or "credit_card". This makes the code easy to extend when adding new payment types.

The Singleton Pattern is used in the PaymentGateway class. It ensures that only one gateway object 
is created and shared in the system. This helps keep the payment process organized and consistent.
"""

from abc import ABC, abstractmethod

# Abstract Base Class for Payment Methods   
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Payment Method Classes
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."
    
class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Bank Transfer."
    
class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Cryptocurrency."
    
class GooglePayPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Google Pay."
    
class ApplePayPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Apple Pay."
    
# Factory Class to create Payment Method instances
class PaymentFactory:
    # Dictionary to map method names to classes
    payment_classes = {
        "credit_card": CreditCardPayment,
        "paypal": PayPalPayment,
        "bank_transfer": BankTransferPayment,
        "crypto": CryptoPayment,
        "google_pay": GooglePayPayment,
        "apple_pay": ApplePayPayment
    }

    @staticmethod
    def get_payment_method(method):
        try:
            return PaymentFactory.payment_classes[method]()
        except KeyError:
            raise ValueError(f"Unknown payment method: {method}")
        
    def paymentGateway(self, method, amount):
        payment_method = PaymentFactory.get_payment_method(method)
        return payment_method.pay(amount)
    
# Singleton Class for Payment Gateway
class Gateway:
    __instance = None

    def __new__(cls):
        # Ensure only one instance is created
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def process_payment(self, method, amount):
        payment_method = PaymentFactory.get_payment_method(method)
        return payment_method.pay(amount)
    
# Main function to demonstrate functionality
if __name__ == "__main__":
    gateway1 = Gateway()
    gateway2 = Gateway()

    print(gateway1 is gateway2)  # True, both are the same instance
    
    print(gateway1.process_payment("credit_card", 100))
    print(gateway1.process_payment("paypal", 200))
    print(gateway1.process_payment("bank_transfer", 300))
    print(gateway1.process_payment("crypto", 600))
    print(gateway1.process_payment("google_pay", 500))
    print(gateway1.process_payment("apple_pay", 300))