from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/res", methods=['POST'])
def res():
	"""Respond to incoming calls with a simple text message."""
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey")
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
