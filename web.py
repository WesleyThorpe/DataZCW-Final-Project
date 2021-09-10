from datetime import date
from sqlite3.dbapi2 import Date
import requests
from flask import Flask, render_template, request
import sqlite3



conn = sqlite3.connect('database', check_same_thread=False)
c = conn.cursor()



app = Flask(__name__)
app.debug = True






@app.route('/', methods=['GET', 'POST'])
def dropdown():
    #sports = ['Baseball', 'Basketball', 'Football', 'Hockey']
    #location = ['Philadelphia', 'Boston', 'Miami', 'Los Angeles', 'Milwaukee', 'Charlotte', 'Detriot', 'Toronto', 'Tampa']
    #return render_template('sports.html', sports=sports, locations=location)
    if request.method=='POST':
        sports=request.form.get("sports")
        location=request.form.get("location")
        date=request.form.get("date")
        if sports == "MLB":
            c.execute( "SELECT * from MLB WHERE location like '%{loc}%' AND date like '%{dt}%' ORDER by date limit 1".format(loc = location, dt = date))
        elif sports == "NHL":
            c.execute("SELECT * from NHL WHERE location like '%{loc}%' limit 1".format(loc = location, dt = date))
        elif sports == "NBA":
            c.execute("SELECT * from NBA WHERE location like '%{loc}%' AND date like '%{dt}%' ORDER by date limit 1".format(loc = location, dt = date))
        elif sports == "NFL":
            c.execute("SELECT * from NFL WHERE location like '%{loc}%' AND date like '%{dt}%' ORDER by date limit 1".format(loc = location, dt = date))
        results= c.fetchall()
        return render_template("sports.html", results=results, sports=sports, location=location, date=date) 
    elif request.method=='GET':
        All_Dates = set()
        Date_Tuples = []
        Date_Tuples.extend(c.execute("SELECT DISTINCT date from MLB").fetchall())
        Date_Tuples.extend(c.execute("SELECT DISTINCT date from NHL").fetchall())
        Date_Tuples.extend(c.execute("SELECT DISTINCT date from NBA").fetchall())
        Date_Tuples.extend(c.execute("SELECT DISTINCT date from NFL").fetchall())
        for d in Date_Tuples:
            All_Dates.add(d[0])
        final_dates = sorted(list(All_Dates))   
        return render_template("sports.html") 
  


if __name__ == "__main__":
    app.run()