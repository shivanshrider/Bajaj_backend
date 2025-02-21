from flask import Flask, request, jsonify

app = Flask(__name__)

# Exception handling function
def handle_exception(e):
    """Global exception handler for unexpected errors."""
    return jsonify({
        "is_success": False,
        "error": str(e)
    }), 400

app.register_error_handler(Exception, handle_exception)

@app.route('/')
def home():
    """Home route to check if the API is working."""
    return jsonify({"message": "API is working!"}), 200

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        # Get JSON data from POST request
        data = request.get_json()

        # Validate if 'data' key exists in the request
        if not data or "data" not in data:
            raise ValueError("Missing 'data' field in the request")

        input_data = data["data"]

        # Ensure 'data' contains a list
        if not isinstance(input_data, list):
            raise TypeError("'data' field must be a list.")

        # Separate numbers and alphabets
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]

        # Find the highest alphabet (case insensitive)
        highest_alphabet = max(alphabets, key=lambda x: x.lower(), default=None)

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic logic if needed
            "email": "john@xyz.com",         # Replace with dynamic logic if needed
            "roll_number": "ABCD123",        # Replace with dynamic logic if needed
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }

        return jsonify(response), 200
    except Exception as e:
        # Exception handling
        return handle_exception(e)

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    # Expected GET response body
    return jsonify({"operation_code": 1}), 200

if __name__ == '_main_':
    app.run(debug=True)