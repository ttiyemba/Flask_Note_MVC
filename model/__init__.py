from app import app
from flask_sqlalchemy import SQLAlchemy

#database+driver://username:password@ipaddress:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:backendboys@34.76.46.214:3306/note"
db = SQLAlchemy(app)