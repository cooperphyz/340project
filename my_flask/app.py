from flask import Flask, render_template, request, flash, redirect
import os
import database.db_connector as db
from database.db_connector import connect_to_database, execute_query

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
    print("Fetching teachers data")
    db_connection = connect_to_database()
    query = "SELECT teacherID, teacherID, first_name, last_name, email FROM Teachers ORDER BY teacherID;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    
    if request.method == 'POST':
    	teacherID = request.form['teacherid']
    	first_name = request.form['firstname']
    	last_name = request.form['lastname']
    	email = request.form['email']

    	data = (teacherID, first_name, last_name, email)
    	teacher_query = "INSERT INTO Teachers (teacherID, first_name, last_name, email) VALUES (%s,%s,%s,%s)"
    	try:
    	    execute_query(db_connection, teacher_query, data)
    	    flash('Teacher Added!', 'success')
    	    return redirect('/teachers')
    	except:
    	    flash('There was an error adding the teacher...')

    return render_template('teachers.html',rows=result)

@app.route('/teacher_update/<int:id>', methods=['GET', 'POST'])
def teacher_update(id):
    db_connection = connect_to_database()
    if request.method == 'GET':

        teacher_query = "SELECT teacherID, teacherID, first_name, last_name, email FROM Teachers WHERE teacherID = %s" % (id)
        teacher_result = execute_query(db_connection, teacher_query).fetchone();

        if teacher_result == None:
            return "No such teacher found"
        else:
            return "Update Page Work in Progress"
    


@app.route('/students', methods=['GET', 'POST'])
def students():
    print("Fetching students data")
    db_connection = connect_to_database()
    query = "SELECT studentID, studentID, first_name, last_name, email FROM Students ORDER BY studentID;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    if request.method == 'POST':
    	studentID = request.form['studentid']
    	first_name = request.form['firstname']
    	last_name = request.form['lastname']
    	email = request.form['email']

    	data = (studentID, first_name, last_name, email)
    	student_query = "INSERT INTO Students (studentID, first_name, last_name, email) VALUES (%s,%s,%s,%s)"
    	try:
    	    execute_query(db_connection, student_query, data)
    	    flash('Student Added!', 'success')
    	    return redirect('/students')
    	except:
    	    flash('There was an error adding the student...')

    return render_template('students.html',rows=result)

@app.route('/courses', methods=['GET', 'POST'])
def courses():
    print("Fetching courses data")
    db_connection = connect_to_database()
    query = "SELECT crn, crn, name, subject, roomNumber FROM Courses ORDER BY crn;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    if request.method == 'POST':
    	crn = request.form['crn']
    	name = request.form['coursename']
    	subject = request.form['subject']
    	classroom = request.form['classroom']

    	data = (crn, name, subject, classroom)
    	course_query = "INSERT INTO Courses (crn, name, subject, classroom) VALUES (%s,%s,%s,%s)"
    	try:
    	    execute_query(db_connection, course_query, data)
    	    flash('Course Added!', 'success')
    	    return redirect('/courses')
    	except:
    	    flash('There was an error adding the course...')

    return render_template('courses.html',rows=result)

@app.route('/classrooms', methods=['GET', 'POST'])
def classrooms():
    print("Fetching classrooms data")
    db_connection = connect_to_database()
    query = "SELECT roomNumber, roomNumber, building, capacity FROM Classrooms ORDER BY roomNumber;"
    result = execute_query(db_connection, query).fetchall();
    print(result)

    if request.method == 'POST':
    	roomNumber = request.form['roomnumber']
    	building = request.form['building']
    	capacity = request.form['capacity']

    	data = (roomNumber, building, capacity)
    	classroom_query = "INSERT INTO Classrooms (roomNumber, building, capacity) VALUES (%s,%s,%s)"
    	try:
    	    execute_query(db_connection, classroom_query, data)
    	    flash('Classroom Added!', 'success')
    	    return redirect('/classrooms')
    	except:
    	    flash('There was an error adding the student...')

    return render_template('classrooms.html',rows=result)