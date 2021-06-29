from flask import Flask, render_template, request
from cryptography.fernet import Fernet


app = Flask(__name__)

key = Fernet.generate_key()
  
# value of key is assigned to a variable
f = Fernet(key)
  
# the plaintext is converted to ciphertext
token = f.encrypt(b"welcome to geeksforgeeks")
d = f.decrypt(token)
#http://127.0.0.1:5000/

@app.route('/')
def index():
    return render_template(
        'index.html' ,
        # d = f.decrypt(token),
        name=token

    )
    
@app.route('/d')
def index1():
    return render_template(
        'index.html' ,
        name3 = d
        
    )
    
# @app.route('/encrypt?string=<string_to_encrypt>')
# def index1():
#     return render_template(
#         'index.html' ,
#         name3='adf9420-12fnkadl;f=4fjmqe' ,
#     )
    


#@app.route('/encrypt?string=<string_to_encrypt>')
#def get_index():
#    return "<strong>Its index page<strong>"



@app.route('/catalog')
def get_catalog():
    return render_template('catalog.html')
    
    

@app.route('/row/<item>')
def get_row(item='Default value'):
    return render_template('item.html', item=item)
    
    
    
@app.route('/product')
def get_product_by_args():
    item = request.args.get('item', 'Default value')

    return render_template('item.html', item=item)



if __name__ == '__main__':
    app.run(debug=True)