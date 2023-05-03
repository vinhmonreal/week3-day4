import unittest
from shoping_cart import Cart

class Test_Cart(unittest.TestCase):
    def test_add(self):
        a = Cart()
        a.item = 'egg'
        a.price = 0.5
        a.quantity = 10
        a.add()
        self.assertEqual(a.grocery_dict, {'egg':{'quantity': 10, 'price': 0.5}})
    def test_remove(self):
        a = Cart()
        a.item_to_remove = 'egg'
        a.quantity = 5
        a.remove()
        self.assertEqual(a.grocery_dict, {'egg':{'quantity': 5, 'price': 0.5}})
        
    def test_total(self):
        a = Cart()
        a.grocery_dict = {'egg':{'quantity': 5, 'price': 0.5},'apple':{'quantity': 10, 'price': 1}}
        self.assertEqual(a.total(), 12.5)
    
if __name__ == '__main__':
    unittest.main()