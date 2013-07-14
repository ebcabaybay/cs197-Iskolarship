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
from models import Students
from models import Programs
from database import db_session, db_init
import traceback
import os

UPLOAD_FOLDER = '/var/uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db_init()

# TRY
@app.route('/students/<int:studentid>/', strict_slashes=False)
def get_student(studentid):
    try:
        student = db_session.query(Student).filter_by(studentid=studentid).one()
	return student.reasonforneedingscholarship
    except sqlalchemy.orm.exc.NoResultFound:
        return 'Message does not exist', 404

# Function that maps to HTTP GET requests
# Example: accessing localhost:8080/messages/1
# Used in RESTful services to get objects
# By default, if we don't specify a methods attribute
# the handlers only respond to GET
@app.route('/messages/<int:id>/', strict_slashes=False)
def get_message(id):
    try:
        message = db_session.query(Message).filter_by(id=id).one()
        return message.message
    except sqlalchemy.orm.exc.NoResultFound:
        return 'Message does not exist', 404

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

@app.route('/getstudentdetails/<int:studentid>/', methods=['GET'], strict_slashes=False)
def get_astudentdetails(studentid):
	try:
		students = db_session.query(Students).filter_by(studentid=studentid).one()
		persons = db_session.query(Persons).filter_by(personid=students.personid).one()
		programs = db_session.query(Programs).filter_by(programid=students.programid).one()
		infohere = persons.firstname + ' ' + persons.middlename + ' ' + persons.lastname + '_' + programs.name + '_' + students.reasonforneedingscholarship + '_' + str(students.targetmoney)
		return infohere
	except sqlalchemy.orm.exc.NoResultFound:
		return 'There are no persons', 404

if __name__ == '__main__':
    print 'Listening on port 8080...'
    app.run(host='0.0.0.0', port=8080, debug=True)
