from shopping_text import options as opt
from shopping_text import text as txt

class Cart():
    def __init__(self):
        self.cart = []
        
        # Added decrease option because we can have multiple identical name entries
    def decrease_product(self, product):
        for item in self.cart:
            if item.name == product:
                reduce = input(txt['reduce'].format(quantity=item.quantity, product=product))
                item.quantity -= int(reduce)
                print('{reduce} {product} removed. you now have {quantity} {name} in your cart.'.format(reduce=reduce, product=product, quantity=item.quantity, name=product))
        return
        
        print(txt['delete_error'].format(product=product.title()))

    def add_product(self, product):
            self.cart.append(product)
            print(txt['add_success'].format(name=product.name.title()))
        
    def show_cart(self): 
        print(txt['cart_divider'])

        total = 0
        for product in self.cart:
            item_total = product.quantity * product.price
            # Changed keys to match what was in the text file
            print(txt["item_line"].format(key=product.name.title(),quantity=product.quantity, item_total=item_total))
            total += item_total
        print(txt['total_line'].format(total=total))

        print(txt['cart_divider'])
    
    def delete_product(self, product):
        # if product ==  product.name in product_list:
        for item in self.cart:
            if item.name == product:
                self.cart.remove(item)
                print(f'{product} removed')
                break
 
        print(txt['delete_error'].format(product=product.title()))

    @property
    def total(self):
        result = [product.item_total for product in self.cart]
        return sum(result)
    
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self. quantity = quantity
        self.price = price

    @property
    def item_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.name.title()

def main():
    # instantiating the class of Cart and making a persistent list for the products
    shopping_cart = Cart()
    application_running = True
    while application_running == True:

        # text prompt for task
        choice = input(txt['main_prompt']).lower().strip()
        if choice in opt['show_options']:
            shopping_cart.show_cart()

        # input prompts for adding to cart
        elif choice in opt['add_options']:
            product = input(txt['add_name']).lower().strip()
            quantity = int(input(txt['add_quantity']))
            price = float(input(txt['add_price']))
            product = Product(product, quantity, price)
            shopping_cart.add_product(product)

         # input prompts for deleting from the  cart
        elif choice in opt['delete_options']:
            product = input(txt['delete_name']).lower().strip()
            shopping_cart.delete_product(product)

        # input prompts for quitting
        elif choice in opt['quit_options']:
            print(txt['quit_message'])
            shopping_cart.show_cart()
            application_running = False

        # input prompts for reducing the quantity of an item already in the cart
        elif choice in opt['reduce_options']:
            product = input(txt['reduce_name']).lower().strip()
            shopping_cart.decrease_product(product)

        input(txt["continue"])

# main()