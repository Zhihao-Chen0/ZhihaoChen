from abc import ABC, abstractmethod

# Payment Processor Interface and Concrete Implementations
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Concrete Payment Processors
class PaypalPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing payment of ${amount} through PayPal."
    
class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing payment of ${amount} through Stripe."
    
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing payment of ${amount} through Credit Card."

# Factory for creating payment processors
class PaymentFactory:
    payment_classes = {
        "paypal": PaypalPayment,
        "stripe": StripePayment,
        "credit_card": CreditCardPayment
    }
    # Static method to get the appropriate payment processor
    @staticmethod
    def get_processor(payment_method):
        try:
            return PaymentFactory.payment_classes[payment_method]()
        except KeyError:
            raise ValueError(f"Unknown payment method: {payment_method}")
    
    @staticmethod
    def checkout(payment_method, amount):
        processor = PaymentFactory.get_processor(payment_method)
        return processor.process_payment(amount)
    
# Main function
if __name__ == "__main__":
    try:
        print(PaymentFactory.checkout("paypal", 100))
        print(PaymentFactory.checkout("stripe", 200))
        print(PaymentFactory.checkout("credit_card", 300))
        print(PaymentFactory.checkout("bitcoin", 400))  # This will raise an error
    except ValueError as e:
        print("Error:", e)