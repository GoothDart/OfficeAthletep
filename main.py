from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from config import host, password, db_name, user
connection = pymysql.connect(
    host= host,
    password= password,
    user= user,
    database= db_name,
    port= 3306,
    cursorclass= pymysql.cursors.DictCursor)
main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://std_2318_officeathlete:officeadmin@std-mysql/std_2318_officeathlete'
db = SQLAlchemy(main)
@main.route('/', methods= ['POST', 'GET'])
@main.route('/index', methods= ['POST', 'GET'])
def index():

    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT `text_of_exercise` FROM `exercise` WHERE `id` = 1')
    #     global str1 = cursor.fetchall()

    return render_template('main.html', exercise.query.all())
