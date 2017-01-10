from flask import Flask, render_template,request,jsonify
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from MySQLdb import escape_string as thwart
import MySQLdb
from twilio.rest import TwilioRestClient
from twilio import twiml
from flask.ext.mysql import MySQL
import os
import requests,time
import json
import datetime
import twilio.twiml
import jsonschema
#from routes.cname import MyName
from flask_restful import Resource, Api

import os





app = Flask(__name__)



#api = Api(app)

mysql = MySQL()
 
@app.route("/")
def main():
   # return "Welcome!"
  return render_template('home.html')

@app.route('/sms', methods=['POST','GET']) 
def sms():
	ACCOUNT_SID = "AC7f31123e044d86fcbaf0934dc66c6788" 
	AUTH_TOKEN = "c732383c7be727ce64b2d3bff60e8724"
	slist = str(request.form['slist'])
	rlist = str(request.form['rlist'])
	msg= str(request.form['msg'])
	print slist,rlist,msg
	
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	db = MySQLdb.connect( host="localhost",user="root",passwd="root",db="twilio" )
	cur = db.cursor()
	slist = request.form['slist']
	rlist = request.form['rlist']
	msg= request.form['msg']
	now=datetime.datetime.now()
	senttime=now.strftime("%Y-%m-%d %H:%M:%S")
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	msg1=client.messages.create(to=rlist, from_=slist, body=msg,status_callback="http://requestb.in/x19o8ex1")
	msg1_sid=msg1.sid
	print dir(msg1)
	print msg1.direction
	print msg1_sid
	print msg1.status 


	query="""INSERT into send(sender,recever,message,senttime,msg_sid)values(%s,%s,%s,%s,%s)"""
	cur.execute(query,(slist,rlist,msg,senttime,msg1_sid))
	print "Record successfully added"
	db.commit()
	cur.close()
	db.close()

	#return render_template('register.html')
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey. What are u doing!!!!!!!")
	return str(resp)



if __name__ == "__main__":
 app.run(host='localhost', debug=True, port=5050)