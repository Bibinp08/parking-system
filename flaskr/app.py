import json
import logging
from flaskr.send import send_message
from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.route("/create_token", methods=["POST"])
def create_token():
    try:
        body = request.json
        if not body:
            return jsonify({"error": "request body not found"}), 400
        queue_message = json.dumps({"carNum": body["carNum"], "name": body["name"]})
        send_message(queue_message)
        logging.info(f"Started creating token for {body['carNum']}")
        return jsonify({"success": True})
    except KeyError as ex:
        logging.exception(
            f"error = {ex}")
        abort(500)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
