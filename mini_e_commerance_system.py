# order_system.py

class Order:
    def __init__(self, customer, country, weight, is_vip):
        self.customer = customer
        self.country = country
        self.weight = weight
        self.is_vip = is_vip

    def calculate_shipping_fee(self):
        # shipping by country
        if self.country == "KR":
            fee = self.weight * 100
        elif self.country == "US":
            fee = self.weight * 300
        else:
            fee = self.weight * 500

        # discount
        if self.is_vip:
            fee = fee * 0.8

        return fee

    def print_order(self):
        print("Customer:", self.customer)
        print("Country:", self.country)
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
order = Order("Alice", "KR", 10, True)
order.print_order()

payment = PaymentProcessor()
payment.process_payment("credit", order.calculate_shipping_fee())