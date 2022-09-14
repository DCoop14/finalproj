from app import app
from flask import render_template, request
from requests import request as fetch
from app.models import db, Contribution
from flask_login import current_user

@app.route('/')
def index():
    user = [{'name': 'CareNow','img': 'https://i0.wp.com/loudounnow.com/wp-content/uploads/2017/07/Unknown.png?fit=225%2C225&ssl=1'}]

    return render_template('index.html', names=user)

@app.route('/charities')
def contact():
    res = fetch(method='GET', url='https://api.data.charitynavigator.org/v2/Organizations?app_id=ee6df4b0&app_key=97f2f6a8fb49596ad5fe1cbd69f23c0e')
    charities = res.json()
    return render_template('charities.html', charities=charities)


@app.route('/charities/create', methods=['GET','POST'])
def contact_create(): 
    res = fetch(method='GET', url='https://api.data.charitynavigator.org/v2/Organizations?app_id=ee6df4b0&app_key=97f2f6a8fb49596ad5fe1cbd69f23c0e')
    charities = res.json()
    print(charities)
    user = current_user.id 
    if request.method =='POST':
        if request.form.get('contribute') == 'donate':
            amount = request.form.get('amount')
            charity_id = request.form.get('charity_id')
            print(amount, charity_id)
            c = Contribution(amount, charity_id, user)
            db.session.add(c)
            db.session.commit()
            return render_template('charities.html', user=user, charities=charities)




    # print(request.form)
    # charity_id = request.form['charity_id']
    # user_id = request.form['user_id']
    # amount = request.form['amount']
    # contribution = models.Contribution(amount=amount, charity_id=charity_id, user_id=user_id)
    # contribution
    return render_template('charities.html', user=user, charities=charities)

    
    
