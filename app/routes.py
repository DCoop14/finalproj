from app import app
from flask import render_template, request
from requests import request as fetch
from app.models import db, Contribution, Goal
from flask_login import current_user

@app.route('/')
def index():
    user = [{'name': 'CareNow','img': 'https://i0.wp.com/loudounnow.com/wp-content/uploads/2017/07/Unknown.png?fit=225%2C225&ssl=1'}]

    return render_template('index.html', names=user)


@app.route('/charities/<ein>')
def charity(ein):
    res = fetch(method='GET', url=f"https://api.data.charitynavigator.org/v2/Organizations/{ein}?app_id=ee6df4b0&app_key=97f2f6a8fb49596ad5fe1cbd69f23c0e")
    charities = [res.json()]
    return render_template('charities.html', charities=charities)


@app.route('/charities', methods=['GET','POST'])
def charities():
    res = fetch(method='GET', url='https://api.data.charitynavigator.org/v2/Organizations?app_id=ee6df4b0&app_key=97f2f6a8fb49596ad5fe1cbd69f23c0e')
    charities = res.json()
#     return render_template('charities.html', charities=charities)


# @app.route('/charities/create', methods=['GET','POST'])
# def charity_create(): 
#     res = fetch(method='GET', url='https://api.data.charitynavigator.org/v2/Organizations?app_id=ee6df4b0&app_key=97f2f6a8fb49596ad5fe1cbd69f23c0e')
#     charities = res.json()
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
            # return render_template('charities.html', user=user, charities=charities)
    # print(request.form)
    # charity_id = request.form['charity_id']
    # user_id = request.form['user_id']
    # amount = request.form['amount']
    # contribution = models.Contribution(amount=amount, charity_id=charity_id, user_id=user_id)
    # contribution
    return render_template('charities.html', user=user, charities=charities)

@app.route('/goals', methods=['GET','POST'])
def goals():
#     goals = [{'img': 'img/jpeg;base64,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taRcl1iSd5JKgm6iVx/MD/Ucfk1WfUzVuaidI6V0ZxtaAGFxtYk3JcAhBbUREAREQBfCV9RAeLp2hclXWQlpa/CWkWIcAQQdoIO0LvwDgPBfObHAeCAyTWbVDR7iX085gd7hY6aLuA6TfEjqVLnppqfIFszf0GTX/eYPmv6P5tvAeCc2OAQH85Qve7+5nB/yJD5gLtjoZzshmP8AoS/7V/QPNjgvmAcAgMHboarOynmP+mR9qyktF6rzuN5qee3utdE2/a4uNvBbPhHBfbBAVfRAfAzBFSCJvxtJJ4uOZJ7VJtnnPsgd9/uUsiAi7zHh4lfDHUcW+alUQFdrtESz+uIncCQ647CMwomXUuY+rO1nVgc/7TleEQFEZqJKT06rEOAhLR5PU1Q6vvhbhZPhHBkLG36ztuesqwogI0aLuLOkc4bwQ2x7RZeR1bpTthjPbEz8FLogIY6rUR200X1Av0zVqiGylh/ZNPzCl0QHLHQxNyEbR2NAXqKdnujwXqiA8+abwC/WAcF+kQHzCll9RAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREB//Z'}]

#     return render_template('goals.html', amount=2)


# @app.route('/goals/create', methods=['POST'])
# def goals_create(): 
    user = current_user.id
    
    amount = 10
    latest_goal = Goal(amount, user)
    goals = Goal.query.filter_by(user_id=user).all()
    if (len(goals)>0):
        latest_goal=goals.pop()
        # print(goals.pop())
        amount=latest_goal.amount
    if request.method =='POST':
        if request.form.get('submit') == 'goal':
            amount = request.form.get('amount')
            # charity_id = request.form.get('charity_id')
            # print(amount, charity_id)
            latest_goal.amount=amount
            # g = Goal(amount, user)
            db.session.add(latest_goal)
            db.session.commit()
            # return render_template('goals.html', user=user, amount=amount)
    # print(request.form)
    # charity_id = request.form['charity_id']
    # user_id = request.form['user_id']
    # amount = request.form['amount']
    # contribution = models.Contribution(amount=amount, charity_id=charity_id, user_id=user_id)
    # contribution
    return render_template('goals.html', user=user, amount=amount)    
    
