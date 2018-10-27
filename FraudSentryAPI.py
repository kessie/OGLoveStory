from flask import Flask, url_for, request, make_response
import requests
from Fraudengine import Fraudengine

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/check', methods=['POST'])
def check():
	request_json = request.get_json()
    	username = request_json.get("user")
    	password = request_json.get("password")
    	print username
    	print password
    	Test1 = Fraudengine(username, password)
    	print Test1.CheckFraud() # return from fucntion here 
    	return 'username : ' + username + '  password:' +  password


if __name__ == '__main__':
    app.run()
