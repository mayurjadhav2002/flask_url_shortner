from flask import Flask, request, flash, url_for, redirect, render_template, jsonify, json
from flask_sqlalchemy import SQLAlchemy
import secrets
import string
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url2.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
class url(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   url = db.Column(db.String(100))
   shorted_text = db.Column(db.String(50))
   views = db.Column(db.Integer)
   def __init__(self, url, shorted_text, views):
      self.url = url
      self.shorted_text = shorted_text
      self.views = views

# Main APP
@app.route("/")
def index():
   return render_template('index.html', url = url.query.order_by(url.id.desc()).limit(12).all() )  


# New Page for submitting the Form
# Not needed if you want to submit on same page i.e. Index
@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['url']:
         flash('Please enter all the fields', 'error')
      else:
         res = ''.join(secrets.choice(string.ascii_uppercase +string.ascii_lowercase + string.digits) for i in range(5))
         abc = url(request.form['url'], res, 0)
         
         db.session.add(abc)
         db.session.commit()
         flash(res)
         return redirect('./')
   return render_template('new.html')



# This is redirection root.
@app.route("/<a>")
def data2(a):
   if len(a) != 5:
      return render_template('no_url.html')
   else:
      url1 = url.query.filter_by(shorted_text=a).first_or_404()
      url1.views = url1.views+1
      db.session.commit()
      return redirect(url1.url)
      # return jsonify({  "ID": url1.id,
      #                   "URL": url1.url,
      #                   "Redirect": "http://127.0.0.1:5000/"+url1.shorted_text
      #  })





@app.route("/post")
def change_ip():

   a = request.args.get('addr', '')
   res = ''.join(secrets.choice(string.ascii_uppercase +string.ascii_lowercase + string.digits) for i in range(5))
   abc = url(a, res)
   db.session.add(abc)
   db.session.commit()
   return jsonify({
      "URL" : a,
      "Redirect": "https://127.0.0.1:5000/"+res
   })




@app.route("/getdata/<a>")
def data(a):
   
   url1 = url.query.filter_by(shorted_text=a).first()
   return render_template('view.html', url2=url1)



@app.errorhandler(404)
def not_found(error):
    # return render_template('error.html'), 404
    return render_template('error.html')


@app.route("/app2")
def aspp():
   return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

