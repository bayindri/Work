# to pass arguments from HTML to Server we need 'request' module introduced below
# 'request' determines whether the current HTTP method is a GET or a POST.
from flask import Flask, render_template, request

#the below is a custom class created in forms.py
from forms import ContactForm
 
app2 = Flask(__name__) 

'''the below line to prevent a CSRF attack by making sure that the form submission originates from my web app
configure Flask-WTF to handle a security exploit known as cross-site request forgery (CSRF). 
In a perfect world, your server would only process forms that belong to your web app. 
In other words, your server would only handle and validate the forms that you created. 
However, it is possible for an attacker to create a form on his own website, fill it in 
with malicious information, and submit it to your server. 
If your server accepts this malicious information, all sorts of bad things can happen next.'''
app2.secret_key = 'ayindris secret key'   
 
 
# All the mapping to respective child webpages is happening here
@app2.route('/')
def home():
  return render_template('home.html')
 
@app2.route('/about')
def about():
  return render_template('about.html')
  
#@app.route('/contact')
#def contact():
  #form = ContactForm()
  #return render_template('contact.html', form=form)
 
 
@app2.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
 
#finally running the app
if __name__ == '__main__':
  app2.run(debug=True)