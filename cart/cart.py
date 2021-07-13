


"""This Cart class provide some default behavior that can be inharited or overrided as necessary"""
class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')

        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

