from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app=Flask(__name__)
limiter=Limiter(app,key_func=get_remote_address)
@app.route('/api')
@limiter.limit('1/minute')
def api():
    return "This is the reponse from the API"

if __name__=='__main__':
    app.run(debug=True)
