# Define the classes 

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone_number: str, address: str):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def generate_customer_note(self):
        """ Generates a note about the customer (e.g., order history). """
        pass  


class Product:
    def __init__(self, product_id: str, product_name: str, price: float, stock_availability: bool, category: str):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__stock_availability = stock_availability
        self.__category = category

    def get_product_name(self):
        return self.__product_name

    def get_price(self):
        return self.__price

    def get_stock_availability(self):
        return self.__stock_availability

    def generate_product_info(self):
        """ Generates a summary of the product details. """
        pass  


class Order:
    def __init__(self, order_id: str, order_date: str, customer: Customer, status: str, products: list):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__customer = customer
        self.__status = status
        self.__products = products

    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_products(self):
        return self.__products


class Payment:
    def __init__(self, payment_id: str, amount: float, method: str, credit_card_number: str, cvv: str):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__method = method
        self.__credit_card_number = credit_card_number
        self.__cvv = cvv

    def get_method(self):
        return self.__method

    def get_amount(self):
        return self.__amount


class DeliveryStaff:
    def __init__(self, staff_id: str, name: str, phone_number: str, delivery_status: str, assigned_orders: list):
        self.__staff_id = staff_id
        self.__name = name
        self.__phone_number = phone_number
        self.__delivery_status = delivery_status
        self.__assigned_orders = assigned_orders

    def get_delivery_status(self):
        return self.__delivery_status

    def generate_delivery_info(self):
        """ Generates delivery details for tracking. """
        pass  

# Now, we use these classes to generate the delivery note

# Step 1: is to Create Objects of All Classes

# Create Customer Object
customer1 = Customer(customer_id="C001", name="Galla Salem", email="Gallasalem.2007@gmail.com", phone_number="0123456789", address="New Al Falah City, Abu Dhabi")

# Create Product Objects
product1 = Product(product_id="P001", product_name="Iced Matcha Latte", price=30.0, stock_availability=True, category="Beverage")
product2 = Product(product_id="P002", product_name="Turkey Sandwich", price=22.0, stock_availability=True, category="Food")

# Create Order Object
order1 = Order(order_id="727734", order_date="2025-02-28", customer=customer1, status="Placed", products=[product1, product2])

# Create Payment Object
payment1 = Payment(payment_id="P123", amount=52.0, method="Apple Pay", credit_card_number="4111111111111111", cvv="123")

# Create DeliveryStaff Object
delivery_staff1 = DeliveryStaff(staff_id="D001", name="Jane Smith", phone_number="9876543210", delivery_status="Preparing", assigned_orders=[order1])

# Step 2: to Generate Delivery Note

# Customer Note
customer_note = customer1.generate_customer_note()

# Product Info
product_info = ""
for product in order1.get_products():
    product_info += f"{product.get_product_name()} - {product.get_price()} AED\n"

# Delivery Info
delivery_info = delivery_staff1.generate_delivery_info()

# Output the Delivery Note
print("=== Delivery Note ===")
print(f"Customer Name: {customer1.get_name()}")
print(f"Customer Email: {customer1.get_email()}")
print(f"Customer Address: {customer1.get_address()}")
print(f"Order ID: {order1.get_order_id()}")
print(f"Order Date: {order1.get_order_date()}")
print("Products Ordered:")
print(product_info)
print(f"Payment Method: {payment1.get_method()}")
print(f"Total Amount: {payment1.get_amount()} AED")
print(f"Delivery Status: {delivery_staff1.get_delivery_status()}")
print("======================")
