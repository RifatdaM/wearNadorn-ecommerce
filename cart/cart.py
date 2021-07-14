


"""This Cart class provide some default behavior that can be inharited or overrided as necessary"""
class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')

        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart


    """This function helps to add and update the user basket session data"""
    def add(self, product, qty):
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.session.modified = True


    """This function get the cart data and count the qty of items"""
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())