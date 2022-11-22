import unittest
from VS_shopping_cart import Cart, Product, main
from shopping_text import options as opt
from shopping_text import text as txt
from io import StringIO
from unittest import mock

class ShoppingCartTest(unittest.TestCase):

    def test_add_product(self):
        cart = Cart()
        apples = Product('apples', 7, 1.60)
        bananas = Product('bananas', 60, 0.60)
        cart.add_product(apples)
        cart.add_product(bananas)
        self.assertIn(bananas, cart.cart)
        self.assertIn(apples, cart.cart)
    
    def test_show_cart(self):
        cart = Cart()
        apples = Product('apples', 7, 1.60)
        bananas = Product('bananas', 60, 0.60)
        cart.add_product(apples)
        cart.add_product(bananas)
        cart.show_cart()
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            cart.show_cart()
            self.assertEqual(fake_out.getvalue(), f'''~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~
{apples} x7 ${apples.item_total:.2f}
{bananas} x{bananas.quantity} ${bananas.item_total:.2f}
Total:${cart.total:.2f}
~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~~=~\n''')
            

    def test_delete_product(self):
        cart = Cart()
        apples = Product('apples', 7, 1.60)
        bananas = Product('banana', 60, 0.60)
        cart.add_product(apples)
        cart.add_product(bananas)
        self.assertIn(apples, cart.cart)
        cart.delete_product('apples')
        self.assertNotIn(apples, cart.cart)

    def test_main(self):

        mock_args = ['a', 'apples', '12', 1.69, 'd', 'apples', 'q']
        with mock.patch('builtins.input') as mocked_input:
            mocked_input.side_effect = mock_args
            cart = Cart()
            passed = True
            try:
                result1 = main()
                
            except:
                passed = False
            
            self.assertFalse(passed)

        #  use assert equal and result 

        

unittest.main()