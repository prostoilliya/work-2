from flask import Flask, render_template, request
from cryptography.fernet import Fernet


app = Flask(__name__)
#add the key
key = Fernet.generate_key()
  

f = Fernet(key)
  

token = f.encrypt(b"welcome to geeksforgeeks")
d = f.decrypt(token)
#http://127.0.0.1:5000/

@app.route('/encrypt')
def index():
    return render_template(
        'index.html' ,
        name=token

    )
    
@app.route('/decrypt')
def index1():
    return render_template(
        'index.html' ,
        name3 = d
        
    )

if __name__ == '__main__':
    app.run(debug=True)