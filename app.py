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
from routes.cname import MyName



app = Flask(__name__)

mysql = MySQL()
 
@app.route("/")
def main():
   # return "Welcome!"
  return render_template('index.html')


@app.route('/sndmsg', methods=['POST'])
def sndmsg():
	ACCOUNT_SID = "AC7f31123e044d86fcbaf0934dc66c6788" 
	AUTH_TOKEN = "c732383c7be727ce64b2d3bff60e8724"
	country=str(request.form['countries'])
	phno=str(request.form['ynumber'])
	contain=str(request.form['mnumber'])
	name=str(request.form['name'])
	areaCode=str(request.form['acode'])
	now=datetime.datetime.now()
	datecreation=now.strftime("%Y-%m-%d %H:%M:%S")
	print datecreation,areaCode,name,contain,phno,country
	db = MySQLdb.connect( host="localhost",user="root",passwd="root",db="twilio" )
	cur = db.cursor()
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	numbers = client.phone_numbers.search(
		areaCode=areaCode,
		country=country,
		type="local",
		contains=contain
	)
	if (len(numbers)>0):
		allnumbers=[]
		for i in numbers:
			allnumbers.append(i.phone_number)
			print i.phone_number

			pick=raw_input("pick your number:")
			allnumbers.index(pick)
			#Purchase the first number in the list
			for pick in allnumbers:
				print "congratulations You've picked ",str(pick)
				print "you've purchased ",str(allnumbers.index(pick))
				#numbers[0].purchase()

	else:
		print "sorry no numbers available"

	#
	query="""INSERT into twilioNumbers(Name,phone_number,twilio_number,datecreation)values(%s,%s,%s,%s)"""
	cur.execute(query,(name,phno,pick,datecreation))
	print "Record successfully added"
	db.commit()
	cur.close()
	db.close()
	return jsonify({'numbers':allnumbers}, )
	



if __name__ == "__main__":
 app.run(host='localhost', debug=True, port=5050)    
  




	  
 
# put your own credentials here 
