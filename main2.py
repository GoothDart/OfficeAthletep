from flask import Flask, render_template, url_for, redirect, request
from flask_mysqldb import MySQL
from config import host, password, db_name, user

main = Flask(__name__)

@main.route('/', methods= ['POST', 'GET'])
@main.route('/index', methods= ['POST', 'GET'])
def index():

    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT `text_of_exercise` FROM `exercise` WHERE `id` = 1')
    #     global str1 = cursor.fetchall()

    return "hello"