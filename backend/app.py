from flask import Flask
from flask_cors import CORS
from routes import time_routes
from database import mongo

app = Flask(__name__)
CORS(app)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/exit_time_db"
mongo.init_app(app)

# Register Routes
app.register_blueprint(time_routes, url_prefix="/api/time")

if __name__ == "__main__":
    app.run(debug=True)
