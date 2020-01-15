from flask import Flask,jsonify,request
import email
import json
import re

from email.iterators import typed_subpart_iterator
email_parser = Flask(__name__)

@email_parser.route("/multiply",methods=['GET','POST'])
def index():
	num = int(request.args.get('mul'))
	return jsonify({"result" : num*10})

	#http://127.0.0.1:8410/multiply?mul=5


@email_parser.route("/DeepDive",methods=['POST'])

def find_recev():
	#message = request.get_json()
	
	# {"name":"Amitab" , "location": "USA" , "randomlist": ["a","sefsef","c"] }
	# data=request.get_json()
	# name = data['name']	
	# location = data['location']
	# randomlist = data['randomlist']
	# return jsonify({'name': name , 'location': location , 'randomlist':randomlist[1]})
	data = request.get_json()
	raww = jsonify({'from':data['raw']})

	email_message=email.message_from_string(str(raww)) 

	# abc= email_message['Delivered-To']

	return str(email_message)


@email_parser.route('/')
def hello_world():
    return 'This is DeepDive Api for email_parser!'


if __name__ == '__main__':
    email_parser.run(debug=True,port=8410)