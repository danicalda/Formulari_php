from flask import Flask, render_template
from flask import request
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

mysql = MySQL()

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__': 
    app.run(port = 3000, debug = True)