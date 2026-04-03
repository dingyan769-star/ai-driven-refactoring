# order_system.py
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight):
        pass


class KRShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 100


class USShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 300


class DefaultShipping(ShippingStrategy):
    def calculate(self, weight):
        return weight * 500

class Order:
    def __init__(self, customer, weight, shipping_strategy, is_vip):
        self.customer = customer
        self.weight = weight
        self.shipping_strategy = shipping_strategy
        self.is_vip = is_vip

    def calculate_shipping_fee(self):
        # shipping by country
        fee = self.shipping_strategy.calculate(self.weight)

        if self.is_vip:
            fee *= 0.8

        return fee

    def print_order(self):
        print("Customer:", self.customer)
        print("Weight:", self.weight)
        print("VIP:", self.is_vip)
        print("Shipping Fee:", self.calculate_shipping_fee())


class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit":
            print(f"Processing credit card payment: {amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment: {amount}")
        else:
            print("Unknown payment method")


# usage
strategy = KRShipping()
order = Order("Alice", 10, strategy, True)
order.print_order()

payment = PaymentProcessor()
payment.process_payment("credit", order.calculate_shipping_fee())