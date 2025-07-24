from flask import Flask
app=Flask(__name__)
@app.route('/home')
def home():
     return"hlo bhai"
if __name__=='__main__':
   app.run()