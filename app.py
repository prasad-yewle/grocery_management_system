from flask import Flask,render_template,redirect,request,url_for
import database as db
from model import Grocery
import os
app = Flask(__name__)

#Mapping default URL of app
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/home')
def home():
    return render_template('home.html')  

@app.route('/groclist')
def showgrocs():
    groclist = db.getGroclist()
    return render_template('groclist.html',groclist = groclist)

@app.route('/searchbytype',methods=['POST'])
def searchbytype():
    types = str(request.form['grocType'])
    groclist = db.getGroclist()
    return render_template('searchbytype.html',groclist=groclist,types=types) 
 
@app.route('/addgroc')
def addgroc():
    groc = Grocery()
    return render_template('addgroc.html',groc=groc,action='Add')

@app.route('/deletegroc/<int:grocId>')
def deletegroc(grocId):
    db.deleteGroc(grocId)
    return redirect('/groclist')

@app.route('/editgroc/<int:grocId>')
def editgroc(grocId):
    groc = db.getGrocById(grocId)
    return render_template('addgroc.html',groc=groc,action='Edit')

@app.route('/updategroc',methods=['POST'])
def updatename():
    #Fetch all details of HTML forms
    _id = request.form['grocId']
    name = request.form['grocName']
    price = request.form['grocPrice']
    imgfile = request.files['grocImg']
    types = request.form['grocType']
    quantity = request.form['grocQuantity']

    imgname = imgfile.filename
    path = os.path.join('static\\uploadimg',imgname)
    imgfile.save(path)

    #Create object of form details
    groc = Grocery(_id,name,price,imgname,types,quantity)

    #update the details in db
    db.updateGroc(_id,groc)
    return redirect(url_for('showgrocs'))

@app.route('/savegroc',methods=['POST'])
def savegroc():

    #fetch details of HTML form
    name = request.form['grocName']
    price = request.form['grocPrice']
    types = request.form['grocType']
    quantity = request.form['grocQuantity']

    imgfile = request.files['grocImg']

    imgname = imgfile.filename
    path = os.path.join('static\\uploadimg',imgname)
    imgfile.save(path)

    #create object of form details
    groc = Grocery(name=name,price=price,img=imgname,types=types,quantity=quantity)
    db.saveGroc(groc)
    return redirect(url_for('showgrocs'))

@app.route('/sortname')
def sortname(): 
    groclist = db.getGroclist()
    sort_name = groclist.sort(key=lambda groc:groc.grocName)
    showgrocs()
    return render_template('sort.html',groclist=groclist)

@app.route('/sortprice')
def sortprice(): 
    groclist = db.getGroclist()
    sort_price = groclist.sort(key=lambda groc:groc.grocPrice)
    showgrocs()
    return render_template('sort.html',groclist=groclist)

@app.route('/sorttype')
def sorttype(): 
    groclist = db.getGroclist()
    sort_type = groclist.sort(key=lambda groc:groc.grocType)
    showgrocs()
    return render_template('sort.html',groclist=groclist)

@app.route('/login', methods=['GET', 'POST'])
def log_in():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

    
@app.route('/logout',methods=['GET', 'POST'])
def log_out():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('logout.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)