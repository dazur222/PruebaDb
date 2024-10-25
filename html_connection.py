from flask import Flask, request, render_template, redirect, url_for
import db_methods

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_post', methods = ['POST'])
def login_post():
    user = request.form['user']
    email = request.form['email']
    password = request.form['password']

    if db_methods.is_usuario(user,email,password):
        return redirect(url_for('my_cattle',user = user))
    else:
        return render_template('login.html')
    

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup_post', methods = ['POST'])
def signup_post():
    user = request.form['user']
    email = request.form['email']
    password = request.form['password']

    db_methods.add_user(user,email,password)

    return redirect(url_for('my_cattle',user = user))


@app.route('/mycattle')
def my_cattle():
    user = request.args.get('user')
    return render_template('my_cattle.html',user = user)

if __name__ == '__main__':  
    app.run(debug=True)

#hola