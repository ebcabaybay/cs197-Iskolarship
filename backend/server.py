# Welcome to our simple demo server!
import json # This is a library for encoding objects into JSON
from flask import Flask, request # This the microframework library we'll use to build our backend.
from flask import redirect, url_for
from werkzeug import secure_filename
#from werkzeug import save
import sqlalchemy
from models import Message
from models import Persons
from models import Scholarships
from database import db_session, db_init
import traceback
import os

UPLOAD_FOLDER = '/var/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db_init()


##dan
def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
		
@app.route('/postscholarship/', methods=['POST'], strict_slashes=False)
def postscholarship():
	try:
		xtitle = request.form['title']
		xdescription = request.form['description']
		
		#### start: optional tags
		if request.form.get('degree_cb'):
			xprogram = request.form['degree_choice']
		else:
			xprogram = None
			
		if request.form.get('gender_cb'):
			xgender = request.form['gender_choice']
		else:
			xgender = None
			
		if request.form.get('year_cb'):
			xyearlv = request.form['year_choice']
		else:
			xyearlv = None
			
		if request.form.get('income_cb'):
			xmaxincome = int(request.form['max_income'])
		else:
			xmaxincome = None
		#### end: optional tags

		s = Scholarships(title=xtitle,description=xdescription,program=xprogram,gender=xgender,yearlv=xyearlv,maxincome=xmaxincome)
		db_session.add(s)
		db_session.commit()
		
		file = request.files['file']
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join('/var/uploads/', filename))

		return redirect('http://localhost:8000')
	except:
		db_session.rollback()
		return traceback.format_exc()

@app.route('/poststudentdetails/', methods=['POST'], strict_slashes=False)
def post_studentdetails():
	lastname = request.json['lastname']
	firstname = request.json['firstname']
	p = Persons(lastname=lastname, firstname=firstname)
	db_session.add(p)
	db_session.commit()
	return 'Ok na'

@app.route('/poststudentdetails/<int:personid>/', methods=['GET'], strict_slashes=False)
def get_studentdetails(personid):
	try:
		persons = db_session.query(Persons).filter_by(personid=personid).one()
		rperson = [persons.lastname, persons.firstname]
		return rperson[0]
	except sqlalchemy.orm.exc.NoResultFound:
		return 'There are no persons', 404
if __name__ == '__main__':
    print 'Listening on port 8080...'
    app.run(host='0.0.0.0', port=8080, debug=True)
