import pyrebase
from flask import Flask, render_template, url_for, flash, redirect,request
app = Flask(__name__)
#import pyrebase
#from flask_sqlalchemy import SQLAlchemy
#from forms import RegistrationForm, LoginForm
app.config['SECRET_KEY'] ='a44b1044951256213bb0d017a25567d2'

config = {
    "apiKey": "AIzaSyAAde_VOXKVeZMz5jmASef3U8fxYle9eVE",
    "authDomain": "sportweb-69559.firebaseapp.com",
    "databaseURL": "https://sportweb-69559.firebaseio.com",
    "projectId": "sportweb-69559",
    "storageBucket": "sportweb-69559.appspot.com",
    "messagingSenderId": "248696885006",
    "appId": "1:248696885006:web:2127084e2759638874d15f",
    "measurementId": "G-B5XYMCCQHE"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#storage = firebase.storage()

#file = input('Enter the name of the file you want to upload to storage')
#cloudfilename = input('Enter the name for the file storage')
#storage.child(cloudfilename).put(file)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)
#config = {
 #    "apiKey": "AIzaSyCFhZt6gU0I3O936G37721I5xot7nVsqZU",
  #  "authDomain": "damsy-9c30f.firebaseapp.com",
   # "databaseURL": "https://damsy-9c30f.firebaseio.com",
    #"projectId": "damsy-9c30f",
    #"storageBucket": "damsy-9c30f.appspot.com",
    #"messagingSenderId": "433492449532",
    #"appId": "1:433492449532:web:25c01202996505ec299f79",
    #"measurementId": "G-ZCPFX67YWW"
#}

#firebase = pyrebase.initialize_app(config)

#auth = firebase.auth()
#email = input('please enter your email\n')
#password =input('please enter your password\n')

#user = auth.create_user_with_email_and_password(email,password)
#user = auth.sign_in_with_email_and_password(email,password)
#auth.get_account_info(user['idToken'])


@app.route("/home",methods=['GET', 'POST'])
def home():
     return render_template("home.html")

@app.route("/about",methods=['GET', 'POST'])
def about():
     return render_template("about.html")

@app.route("/top",methods=['GET', 'POST'])
def top():
     return render_template("top.html")

@app.route("/goal",methods=['GET', 'POST'])
def goal():
     return render_template("goal.html")

@app.route("/assist")
def assist():
     return render_template("assist.html")

@app.route("/dribbles")
def dribbles():
     return render_template("dribblers.html")

@app.route("/redcard")
def redcard():
     return render_template("redcard.html")

@app.route("/yellowcard")
def yellowcard():
     return render_template("yellowcard.html")

@app.route("/fixtures")
def fixtures():
     return render_template("fixtures.html")

@app.route("/injuries")
def injuries():
     return render_template("injuries.html")

@app.route("/table")
def table():
     return render_template("table.html")
@app.route("/", methods=['GET', 'POST'])
@app.route("/register",methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            user = auth.create_user_with_email_and_password(email,password)
            return redirect(url_for('fixtures'))
            #auth.send_email_verification(user['idToken'])
        except:
          print("could not register")
    return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
      message = ""
      if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
             user = auth.sign_in_with_email_and_password(email,password)
             #auth.send_email_verification(user['idToken'])
             user = auth.refresh(user['refreshToken'])
             user_id = user['idToken']
             return redirect(url_for('fixtures'))
             
        except:
          return redirect(url_for('login'))

      return render_template('login.html')


@app.route("/forgetPassword", methods=['GET', 'POST'])
def forgetPassword():
           message = ""
           if request.method == 'POST':
                email = ['name']
                #auth.send_email_verification(user['idToken'])
                user = auth.sign_in_with_email_and_password(email,password)
                auth.send_password_reset_email(email)
                user = auth.refresh(user['refreshToken'])
                user_id = user['idToken']
                return redirect(url_for('fixtures'))
           return render_template('forgetPassword.html')


if __name__=="__main__":
     app.run()


#@app.route("/register", methods=['GET','POST'])
#def register():
 #    form = RegistrationForm()
  #   if form.validate_on_submit():
   #     flash(f'Account created for {form.username.data}!','success')
    #    return redirect(url_for('home'))

     #return render_template("register.html",title="Register", form=form)

#@app.route("/login", methods=['GET','POST'])
#def login():
 #    form = LoginForm()
  #   if form.validate_on_submit():
   #       if form.email.data == 'ricyaalon@gmail.com' and form.password.data == 'ogundabede':
    #           flash(f'You Have Been Logged In!', 'success')
     #          return redirect(url_for('home'))
      #    else:
       #        flash('Login Unsuccessful. Please check username and password','danger')
         
     #return render_template("login.html",title="Login", form=form)


#class User(db.Model):
 #    id = db.Column(db.Integer, primary_key=True)
  #   username = db.Column(db.String(20), unique=True, nullable=False)
   #  email = db.Column(db.String(20), unique=True,nullable=False)
    # image_file = db.Column(db.String(20), nullable=False,default='default.jpg')
     #password = db.Column(db.String(60), nullable= False)
     #posts = db.relationship('Post',backref='author', lazy=True)

     #def __repr__(self):
      #    return f"User('{self.username}','{self.email}','{self.image_file}')"


#class Post(db.Model):
 #    id = db.Column(db.Integer, primary_key=True)
  #   title = db.Column(db.String(100), nullable=False)
   #  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # content = db.Column(db.Text, nullable=False)
     #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

     #def __repr__(self):
      #    return f"Post('{self.title}','{self.date_posted}')"




















