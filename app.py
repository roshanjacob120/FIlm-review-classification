from flask import Flask, render_template,url_for
from flask import request
from ml import machine
from scrapimdb import imdb
from scraprotten import rotten
app = Flask(__name__)

@app.route('/')
def result():
   return render_template('index.html')
@app.route('/',methods=['POST'])
def send():
   filmname=request.form.get('filmname')
   rotten(filmname)
   imdb(filmname)
   rating=str(round(machine()[0]*10,2))
   print(rating)
   if(rating=='-10'):
      return render_template('index.html',tex="Oops could'nt find any reviews!!",film=filmname)
   return render_template('index.html',value=(rating+'/10'),film=filmname)

if __name__ == '__main__':
   app.run(debug = True)