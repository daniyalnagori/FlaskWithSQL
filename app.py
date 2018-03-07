from flask import Flask, render_template
from flaskext.mysql import MySQL
import ccxt
import pyodbc


app = Flask(__name__)

#Congifgration with mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#Connect with SQL server

con = pyodbc.connect(r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=demo1;Trusted_Connection=yes;')

@app.route("/")
def index():
    cursor = con.cursor()
    cursor.execute("select * from abc")
    #data = cursor.fetchone()
    data = cursor.fetchall()
    
    return render_template('index.html',data=data)

@app.route("/about")
def about():
    return render_template('about.html')

app.run(debug=True)