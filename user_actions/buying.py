from flask import render_template,make_response,request
from config import app
import base64
class Buying:
    @classmethod
    @app.route('/goods')
    def goods(self):
        return render_template("goods.html")

    @classmethod
    @app.route('/basket')
    def basket(self):
        goods = request.cookies.get("_basket")
        if goods is not None:
            encode = base64.b64decode(goods).decode('utf-8')
            return encode
        else:
            return "basket is empty"
    @classmethod
    @app.route('/order')
    def order(self):
        return render_template("order.html")



