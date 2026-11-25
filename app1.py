from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# DATABASE CONNECTION

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="Tx",
    port=3306
)

cursor = connection.cursor(buffered=True)

# HOME PAGE
@app.route('/')
def signup():
    return render_template('sign_up_page.html')

@app.route('/form', methods=['POST'])
def form():
    fullname = request.form['fullname']
    username = request.form['username']
    useremail = request.form['useremail']
    dob = request.form['dob']
    country = request.form['country']
    password = request.form['password']
    confirm_password = request.form['confirm_password'] 
    insert_query3 = """
    INSERT INTO signup(fullname, username, useremail, dob, country, password, confirm_password)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    """

    values3 = (fullname, username, useremail, dob, country, password, confirm_password)
 
    cursor.execute(insert_query3, values3)
    connection.commit()
    return render_template('loginpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        useremail = request.form['useremail']
        password = request.form['password']

        query = """
        SELECT * FROM signup
        WHERE useremail = %s AND password = %s
        """

        values = (useremail, password)

        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            return redirect(url_for('index'))
        else:
            error_message = "Invalid Email or Password"
            return render_template('login.html', error=error_message)

    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('onlinemyproject.html')

# FIRST FORM

@app.route('/registor1', methods=['POST'])
def registor1():

    FromPlace = request.form['FromPlace']
    ToPlace = request.form['ToPlace']
    start_date = request.form['start_date']
    End = request.form['End']
    guest = request.form['guest']
    insert_query = """
    INSERT INTO travel_list(FromPlace, ToPlace, start_date, End, guest)
    VALUES(%s, %s, %s, %s, %s)
    """

    values = (FromPlace, ToPlace, start_date, End, guest)
 
    cursor.execute(insert_query, values)
    connection.commit()

    return render_template('registorpage.html')

@app.route('/registor_suscess')
def registor_suscess():
    return render_template('onlinemyproject.html')

# SECOND FORM
@app.route('/book')
def book():
    return render_template('booknowpage.html')

@app.route('/registor2', methods=['GET','POST'])
def registor2():

    name = request.form['name']
    your_email = request.form['your_email']
    phone = request.form['phone']
    place = request.form['place']
    start_date = request.form['start_date']
    person = request.form['person']
    Special_Request = request.form['Special_Request']
    insert_query1 = """
    INSERT INTO book_list(name, your_email, phone, place, start_date, person, Special_Request)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    """

    values1 = (name, your_email, phone, place, start_date, person, Special_Request)

    cursor.execute(insert_query1, values1)
    connection.commit()

    return render_template('bookingpage.html')

@app.route('/book_suscess')
def book_suscess():
    return render_template('onlinemyproject.html')

# RUN APP

if __name__ == '__main__':
    app.run(debug=True)