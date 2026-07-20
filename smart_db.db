from smartphone import Smartphone
from smart_sqlite import PrimaryKeyError


import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/newphone", methods = ["POST","GET"])
def newphone():
    if flask.request.method == "POST" :
        Smartphone_data= dict(flask.request.form)
        try:
            Smartphone(int(Smartphone_data["codeid"]),Smartphone_data["price"],Smartphone_data["marke"],
                   int(Smartphone_data["year"]),float(Smartphone_data["battery"]))
        except(PrimaryKeyError):
            return flask.render_template("error.html")
        return flask.redirect("/")
    return flask.render_template("newphone.html")

@app.route("/phoneslist")
def phoneslist():
    all = Smartphone.allphone()
    return flask.render_template("phoneslist.html",allphone=all)

@app.route("/deletephone", methods=["GET","POST"])
def deletephone():
    if flask.request.method == "POST" :
        codeid = dict(flask.request.form)
        Smartphone.delete(codeid["codeid"])
        return flask.redirect("/phoneslist")        
    return flask.render_template("/deletephone.html")

app.run()