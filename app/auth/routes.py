from flask import Blueprint, render_template, request, redirect, url_for
from .forms import LogInForm, UserCreationForm

# import login functionality
from flask_login import login_user, logout_user, login_required, current_user 
from werkzeug.security import check_password_hash, generate_password_hash


# import models
from app.models import User

auth = Blueprint('auth', __name__, template_folder='authtemplates')

from app.models import db

@auth.route('/login', methods = ["GET", "POST"])
def logMeIn():
    form = LogInForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            # Query user based off of username
            user = User.query.filter_by(username=username).first()
            print(user.username, user.password, user.id)
            # ex 1 , user does not exist
            if user:
                # compare passwords
                if check_password_hash(user.password, password):
                    login_user(user)
                else:
                    print('Incorrect password')

            else:
                # user does not exist
                pass

    return render_template('login.html', form=form)

@auth.route('/logout',)
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))


@auth.route('/signup', methods=["GET", "POST"])
def signMeUp():
    form = UserCreationForm()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = generate_password_hash(form.password.data)
            
    
            print(username, email, password)

            user = User(username, email, password)

            db.session.add(user)
            db.session.commit()

            
            return redirect(url_for('auth.logMeIn'))
        else:
            print('validation failed')
    else:
        print('GET req made')


    return render_template('signup.html', form = form)

# @ig.route('api/posts/create', methods=["POST"])
# 
# def createPostAPI():
#     data = request.json #this is coming from POST request Body

#     title = data['title']
#     caption = data['caption']
#     user_id = data['user_id']
#     img_url = data['img_url']

#     post = Post(title, img_url, caption, user_id)
#     post.save()

#     return {
#         'status' : 'ok',
#         'message' : "Post was successfully created."
#     }




#######  API ROUTES  #############
@auth.route('/api/signup', methods=["POST"])
def apiSignMeUp():
    data = request.json
   

    username = data['username']
    email = data['email']
    password = data['password']

    print(username, email, password)

    # add user to database
    user = User(username, email, password)

    # add instance to our db
    db.session.add(user)
    db.session.commit()
   
    return {
        'status' : 'ok"',
        'message' : f"Successfully created user {username}"
       
    }

@auth.route('/api/login', methods=["POST"])
def apiLogMeIn():
    data = request.json

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if user:
        # checkpassword
        if check_password_hash(user.password, password):
            return {
                'status': 'ok',
                'message' : "You have successfully logged in",
                'data' : {
                    'user' : user(),
                    
                 } 
            }
        return {
            'status' : 'not ok',
            'message' : "Incorrect password."
        }  
    return {
        'status' : 'not ok',
        'message' : 'Invalid username.'
    }  














