import json
import time

from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS

app = Flask(__name__)

# Store the latest number
latest_number = None

def generate_number():
    global latest_number
    while True:
        time.sleep(2)  # Simulate processing time
        if latest_number is not None:
            yield f"data: {latest_number}\n\n"

@app.route('/submit_number', methods=['POST', 'GET'])
def submit_number():
    if request.method == "POST":
        global latest_number
        number = request.form.get('number')
        latest_number = number
        return render_template("form.html")
    return render_template("form.html")

@app.route('/stream_number')
def stream_number():
    return Response(generate_number(), content_type='text/event-stream')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
