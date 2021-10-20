#Import Flask dependency
from flask import Flask

#Create a new Flask app instance
app = Flask(__name__)

# create app route
@app.route('/')
def hello_world():
    return 'Hello world'

#run the flask app
#