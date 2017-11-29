# Django Twiliio
A simple django application which accepts a number and a message body, and sends an sms to the number via Twilio SMS API.

Currently using my personal credentials.

# How to run?

* Clone the repo : `git clone https://github.com/Parth-Vader/TwilDjango.git`
* Create a virtualenv : `virtualenv --python=python3.5 --no-site-packages venv
`
* Activate virtualenv : `. venv/bin/activate`
* Install dependencies : `pip install -r requirements.txt`
* Add your Twilio Account ID and Authentication Token, as well as your Twilio number in [views.py](https://github.com/Parth-Vader/TwilioDjango/blob/master/twilapp/twilsms/views.py) file.
* Run the app via : `python manage.py runserver`
* Go to `127.0.0.1:8000/twilsms` to see the app.
