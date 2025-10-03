from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

# Store received events in memory (for demo)
received_events = []

@app.route("/", methods=["POST"])
def receive_event():
    event = request.get_json(silent=True)
    print("✅ Cloud Run received event:")
    print(json.dumps(event, indent=2))

    # Save minimal info for visualization
    event_record = {
        "file_name": event.get("name"),
        "bucket": event.get("bucket"),
        "time": datetime.datetime.utcnow().isoformat() + "Z"
    }
    received_events.append(event_record)

    return {"status": "processed"}, 200

@app.route("/events", methods=["GET"])
def list_events():
    return jsonify(received_events)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
