from flask import Flask, request, render_template, redirect, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'Friends')


@app.route('/')
def index():
    print "Inside the index method"

    query = "select first_name, last_name, age, created_at from users"
    friends = mysql.query_db(query)
    # warning = 'You must enter a first and last name'

    return render_template('index.html', friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    print "Inside the create method"
    
    split_name = request.form['name'].split()
    if len(split_name) <= 1:
        return redirect('/')
    else:
        first_name = split_name[0]
        last_name = split_name[1]

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'age': request.form['age']
        }

        query = "insert into users (first_name, last_name, age, created_at) values (:first_name, :last_name, :age, now())"

        mysql.query_db(query, data)

    return redirect('/')

app.run(debug=True)