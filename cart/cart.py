from store.models import Product
from decimal import Decimal


"""This Cart class provide some default behavior that can be inharited or overrided as necessary"""
from store.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')

        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart


    """This function helps to add and update the user basket session data"""
    def add(self, product, qty):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.session.modified = True


    """this function collect the product_id in the session data to query the database and return products"""
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    """This function get the cart data and count the qty of items"""
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price'])* item['qty'] for item in self.cart.values())