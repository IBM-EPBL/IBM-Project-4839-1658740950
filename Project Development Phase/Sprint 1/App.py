from flask import Flask,render_template, flash,redirect, url_for,request
app = Flask(__name__)
app.secret_key="hello"

@app.route("/")
def index():
	return render_template("index.html")
	

@app.route("/about")                                      
def about():
	return render_template("about.html")



@app.route('/signup',methods=["post","get"])
def signup():
  return render_template('signup.html')

@app.route("/login")
def login():
  return render_template('login.html')  


if __name__=='__main__':
    app.run(debug=True)