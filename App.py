from flask import Flask, request, redirect, url_for , flash
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)


#MySql Connection
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'flaskcontacts'
mysql = MySQL()
mysql.init_app(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()
    return render_template('index.html' , contacts = data) #passo les dades a index.html 

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['Nom']
        phone = request.form['Telèfon']
        email = request.form['Sol·licitud']
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        mysql.get_db().commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))
        

@app.route('/edit/<id>')
def get_contact(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM contacts WHERE id = %s' , (id))
    data = cursor.fetchall()
    return render_template('edit-contact.html', contact = data[0])
   
@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cursor = mysql.get_db().cursor()
    cursor.execute ("""
    UPDATE contacts
    SET fullname = %s,
        email = %s,
        phone = %s
    WHERE id = %s
    """,(fullname, email, phone, id))
    mysql.get_db().commit()
    flash('Contaact updated successfully')
    return redirect(url_for('Index'))



@app.route('/delete/<string:id>')
def delete_contact(id):
    cursor = mysql.get_db().cursor()
    cursor.execute('DELETE FROM contacts WHERE id = {0}' .format(id))
    mysql.get_db().commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__': 
    app.run(port = 3000, debug = True)