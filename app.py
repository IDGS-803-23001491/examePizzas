from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from models import db
from ventas.routes import ventas

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(ventas)
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app,db)

@app.route("/",methods=["GET","POST"])
@app.route("/index")
def index():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
