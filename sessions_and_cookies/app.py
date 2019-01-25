from flask import Flask, session, render_template, redirect, request, url_for
import database as db

app = Flask(__name__)
app.secret_key = 'Hi;]&a5U"%T/uu)p3ZO'

@app.route('/')
def index():
    if 'email' not in session:
        return 'Hello World! You are not logged in!'
        user= false
    else :
        return 'Hello World! You are: ' + session['email']


@app.route('/users')
def users():
    users = db.get_users()
    return render_template("users.html", result = "Hello", rae = "khan")

@app.route('/login', methods={'GET','POST'})
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if db.check_user(email, password):
            print('logged in')
            session['email'] = email
            return redirect(url_for('index'))
        else:
            return "password or username is incorrect"

    # Get request
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()



# db.initialise()
# db.add_user("sam@gmail.com", "hello", "Sam Pham")
# db.add_user("vi@gmail.com", "hello", "Vi Pham")
# if db.check_user('sam@gmail.com', "ahello"):
#     print("Passed")
# else:
#
#     print("Failed!")