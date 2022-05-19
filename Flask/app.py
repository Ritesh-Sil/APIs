#C:\Users\silri\anaconda3\python
from flask import Flask
#Class is always start with Capital letter

app = Flask(__name__)
#Each Flask object with a unique name.Flask is runnning in specific unique space
#What req its going to understand . Have to tell our app what req its going to understand
#Will use decorator

@app.route('/') #www.google.com/ #Endpoint , '/' means the Home page of the site
#It is a decorator which will be applied on the function below
def home():
    return "Hello, world!"

app.run(port=5000)
#5000 is being used by some other program
#127.0.0.1 --> Is my computer and 5000 is the port that is being used currently.
#http means the browser will be able to access this page.
