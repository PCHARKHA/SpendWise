from flask import Flask, jsonify, request,render_template
from datetime import timedelta
import os

from routes.expenses_routes import expense_bp
from routes.auth_routes import auth_bp
from routes.page_routes import page_bp

from utils.database import init_db

from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours = 1)

jwt = JWTManager(app)

app.register_blueprint(expense_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(page_bp)

init_db()

if __name__ == "__main__":
    app.run(debug=True)