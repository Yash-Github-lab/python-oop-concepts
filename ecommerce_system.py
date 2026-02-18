from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Product class
class Product(ABC):
    """Abstract base class for products"""
    
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    @abstractmethod
    def apply_discount(self, discount_percent):
        """Apply discount - different for different product types"""
        pass


class Electronics(Product):
    """Electronics product class"""
    
    def __init__(self, product_id, name, price, stock, warranty_months):
        super().__init__(product_id, name, price, stock)
        self.warranty_months = warranty_months
    
    def apply_discount(self, discount_percent):
        """Apply discount with max 30% for electronics"""
        max_discount = 30
        actual_discount = min(discount_percent, max_discount)
        return self.price * (1 - actual_discount / 100)
    
    def get_details(self):
        return f"{self.name} - ${self.price} (Warranty: {self.warranty_months} months)"


class Clothing(Product):
    """Clothing product class"""
    
    def __init__(self, product_id, name, price, stock, size, material):
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.material = material
    
    def apply_discount(self, discount_percent):
        """Apply discount with max 50% for clothing"""
        max_discount = 50
        actual_discount = min(discount_percent, max_discount)
        return self.price * (1 - actual_discount / 100)
    
    def get_details(self):
        return f"{self.name} - ${self.price} (Size: {self.size}, Material: {self.material})"


class ShoppingCart:
    """Shopping cart to hold items"""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity):
        """Add product to cart"""
        if product.stock >= quantity:
            self.items.append({"product": product, "quantity": quantity})
            product.stock -= quantity
            return f"Added {quantity} x {product.name} to cart"
        return "Insufficient stock"
    
    def remove_item(self, product_id):
        """Remove product from cart"""
        for item in self.items:
            if item["product"].product_id == product_id:
                item["product"].stock += item["quantity"]
                self.items.remove(item)
                return "Item removed from cart"
        return "Item not found in cart"
    
    def calculate_total(self):
        """Calculate total price"""
        return sum(item["product"].price * item["quantity"] for item in self.items)
    
    def display_cart(self):
        """Display cart contents"""
        if not self.items:
            return "Cart is empty"
        
        details = "Shopping Cart:\n"
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            details += f"  - {product.name} x{quantity}: ${product.price * quantity}\n"
        details += f"Total: ${self.calculate_total()}"
        return details


class Order:
    """Order class to represent a purchase"""
    
    order_counter = 1000
    
    def __init__(self, customer_name, cart):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.customer_name = customer_name
        self.items = cart.items
        self.order_date = datetime.now()
        self.status = "Pending"
    
    def process_payment(self, payment_method):
        """Process payment"""
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        self.status = "Completed"
        return f"Order #{self.order_id}: Payment of ${total} received via {payment_method}"
    
    def get_order_summary(self):
        """Get order summary"""
        summary = f"Order #{self.order_id}\n"
        summary += f"Customer: {self.customer_name}\n"
        summary += f"Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
        summary += f"Status: {self.status}\n"
        summary += "Items:\n"
        
        for item in self.items:
            product = item["product"]
            summary += f"  - {product.name} x{item['quantity']}: ${product.price * item['quantity']}\n"
        
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        summary += f"Total: ${total}"
        return summary


# Usage Example
print("=" * 50)
print("E-COMMERCE SYSTEM EXAMPLE")
print("=" * 50)

# Create products
laptop = Electronics(1, "Laptop", 1200, 5, 24)
shirt = Clothing(2, "T-Shirt", 30, 10, "M", "Cotton")
phone = Electronics(3, "Smartphone", 800, 3, 12)

print(f"\nProducts:")
print(f"  {laptop.get_details()}")
print(f"  {shirt.get_details()}")
print(f"  {phone.get_details()}")

# Create shopping cart
cart = ShoppingCart()
print(f"\n{cart.add_item(laptop, 1)}")
print(f"{cart.add_item(shirt, 2)}")
print(f"{cart.add_item(phone, 1)}")

print(f"\n{cart.display_cart()}")

# Apply discounts
laptop_discounted_price = laptop.apply_discount(25)
print(f"\nLaptop with 25% discount: ${laptop_discounted_price:.2f}")

shirt_discounted_price = shirt.apply_discount(60)  # Will be capped at 50%
print(f"T-Shirt with 60% discount (capped at 50%): ${shirt_discounted_price:.2f}")

# Create and process order
order = Order("John Doe", cart)
print(f"\n{order.process_payment('Credit Card')}")
print(f"\n{order.get_order_summary()}")
