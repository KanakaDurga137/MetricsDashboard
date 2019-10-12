from flask import Flask, render-template
app = Flask(--name--)

@app.route("/")
def index():
	return render-template("HomePage.html")



