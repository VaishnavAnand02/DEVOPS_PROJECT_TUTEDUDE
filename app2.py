
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask,jsonify,render_template,request
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("MONGO_URI")
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.test
collection = db.usercollect

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/api/submit", methods=["POST"])
def submit_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "No data provided"}), 400

        if not data.get("name") or not data.get("email"):
            return jsonify({"success": False, "message": "Name and email are required"}), 400

        res = collection.insert_one(data)
        if res.inserted_id:
            return jsonify({"success": True, "message": "Data submitted successfully"}), 201
        else:
            return jsonify({"success": False, "message": "Insert failed"}), 500

    except Exception as e:
        # Always return JSON with 'success': False
        return jsonify({"success": False, "message": str(e)}), 500
    
@app.route("/success")
def reroute():
    return render_template("divert.html")
    
if __name__ == "__main__":
    app.run(debug=True)
