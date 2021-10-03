from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def form():
	return render_template('tact.html')

@app.route('/submit',methods=['POST'])
def form_post():
	Name 	= request.form.get("user_name")
	Email 	= request.form.get("user_email")
	Password= request.form.get("user_password")
	Age     = request.form.get("user_age")
	Bio     = request.form.get("user_bio")
	Job     = request.form.get("user_job")
	Interest= request.form.get("user_interest")
	return render_template("view.html",name = Name,email = Email,password = Password,age = Age,bio = Bio,job = Job,interest = Interest)		
if __name__ == '__main__':
	app.run()
