from flask import Flask
app=Flask(__name__)
@app.route('/')
def api():
    return 'This is the reponse from the API'
