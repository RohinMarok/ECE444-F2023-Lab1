from flask import Flask 
app = Flask( __name__ ) 
@app.route('/') 
def index(): 
    return 'Hello World!' 

@app.route('/user/')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)