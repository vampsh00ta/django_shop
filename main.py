
from flask import render_template, session,make_response,request
from db import Goods,Orders,db
from config import login_manager,admin,ModelView
from api.api import app
import base64
import threading
import requests

#adminka
admin.add_view(ModelView(Goods,db.session))
admin.add_view(ModelView(Orders,db.session))


def doubler(number):
    """
    A function that can be used by a thread
    """
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    print()
@login_manager.user_loader
def load_user(user_id):
    return  Goods.query.filter_by(id =user_id ).first()

@app.after_request
def add_header(response):
    response.headers['Server'] = ''
    return response




@app.route('/goods')
def goods():
    return render_template("goods.html")

@app.route('/basket')
def basket():
    goods = request.cookies.get("_basket")
    if goods is not None:
            encode = base64.b64decode(goods).decode('utf-8')
            return encode
    else:
        return "basket is empty"


@app.route('/order')
def order():
    return render_template("order.html")
# Buying.goods()
# Buying.basket()
# Buying.order()
if __name__ == '__app__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()
    app.run(host='0.0.0.0')

