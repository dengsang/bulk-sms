from flask import Flask, request, render_template

import africastalking

app = Flask(__name__)

username = "sandbox"
api_key = "ENTER_API_KEY_HERE"
africastalking.initialize(username, api_key)

sms = africastalking.SMS


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        sms_message = request.form['smsMessage']
        phone_number = request.form['phoneNumber']

        print(sms_message)
        print(phone_number)

        response = sms.send(sms_message, [phone_number])
        print(response)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
