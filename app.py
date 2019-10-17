from flask import Flask, render_template, url_for, request,redirect
from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField,SubmitField,TextAreaField
from datetime import date

today = date.today()

x = []
count = 0

class AddWish(FlaskForm):
	titleText = StringField('titleText',render_kw={"placeholder": "Wish Title"})
	WishBox = TextAreaField('WishBox',render_kw={"placeholder": "Wish Description"})
	wishAdd = SubmitField('Add',render_kw={"style": "font-family: monospace;transform: translateY(20px);font-size: 2em;float:left;border: 0px;padding: 10px 0px;width: 50%;height: 57px;border-bottom-left-radius: 30px;"})

app = Flask(__name__)
app.config['SECRET_KEY'] = '85277qwea';

@app.route('/', methods=['GET','POST'])
def index():
	form=AddWish()
	result = request.form
	if form.is_submitted():
		x.append([result['titleText'],result['WishBox'],today.strftime("%d/%m/%y")])
		return redirect('')

	return render_template('index.html',form=form,result=x,len=len(x))