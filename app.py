from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Define your API endpoints as before
@app.route('/')
def home():
    app.logger.info(f"Request received from {request.remote_addr}")
    return "Welcome to my API!"

@app.route('/api/data', methods=['GET'])
def get_data():
    app.logger.info(f"GET request received from {request.remote_addr}")
    sample_data = {
        'name': 'Ram',
        'age': 25,
        'city': 'Kathmandu'
    }
    return jsonify(sample_data)

@app.route('/api/data', methods=['POST'])
def add_data():
    app.logger.info(f"POST request received from {request.remote_addr}")
    new_data = request.get_json()
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)

