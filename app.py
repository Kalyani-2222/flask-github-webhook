from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import pymongo

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

# ✅ MongoDB Atlas connection (replace with your actual cluster URI if different)
client = pymongo.MongoClient(
   client = pymongo.MongoClient("mongodb+srv://Kalyani:Kalyani%40123@cluster0.mongodb.net/webhookDB?retryWrites=true&w=majority")

)

db = client['github_events']
collection = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
    event_data = request.get_json()
    print("✅ Webhook received")

    if not event_data:
        return jsonify({"error": "No data received"}), 400

    event_data['timestamp'] = datetime.utcnow().strftime('%d %B %Y - %I:%M %p UTC')
    collection.insert_one(event_data)
    return jsonify({"message": "Event stored"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    print("📥 Fetching events from MongoDB")
    events = list(collection.find({}, {"_id": 0}))  # Exclude Mongo _id
    return jsonify(events), 200

@app.route('/')
def index():
    return "✅ GitHub Webhook Flask server is running!"

if __name__ == '__main__':
    app.run(debug=True)
