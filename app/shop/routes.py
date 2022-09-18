
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import User, db, Item



shop = Blueprint('shop', __name__, template_folder='shop_template')

@shop.route('/shop', methods=["GET", "POST"])
@login_required
def letsShop():
    item = Item.query.all()
    return render_template('shop.html', item=item)

@shop.route('/cart', methods=["GET", "POST"])
@login_required
def getCart():
    user = User.query.get(current_user.id)
    cart = user.cart.all()
    total = len(cart)
    return render_template('cart.html', cart=cart, user=user, total=total)

@shop.route('/add/<string:name>')
@login_required
def addToCart(name):
    item = Item.query.filter_by(name=name).first()
    current_user.cart.append(item)
    db.session.commit()
    flash('Item added to cart.', 'success')
    return redirect(url_for('shop.letsShop'))

@shop.route('/remove/<string:name>')
@login_required
def clearFromCart(name):
    item = Item.query.filter_by(name=name).first()
    current_user.cart.remove(item)
    db.session.commit()
    flash('Item removed from cart.', 'success')
    return redirect(url_for('shop.getCart'))

@shop.route('/removeall')
@login_required
def clearall():
    item = Item.query.all()
    for i in item:
        if i in current_user.cart:
            current_user.cart.remove(i)
            db.session.commit()
    flash('All Items Removed!', 'success')
    return redirect(url_for('shop.getCart'))
