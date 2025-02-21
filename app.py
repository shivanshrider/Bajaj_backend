from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)



# Exception handling function
def handle_exception(e):
    return jsonify({"is_success": False, "error": str(e)}), 400

app.register_error_handler(Exception, handle_exception)

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        # Get JSON data from POST request
        data = request.get_json()

        if "data" not in data:
            raise ValueError("Missing 'data' field in the request")

        input_data = data["data"]

        # Separate numbers and alphabets
        numbers = [item for item in input_data if item.isdigit()]
        alphabets = [item for item in input_data if item.isalpha()]

        # Find the highest alphabet
        highest_alphabet = max(alphabets, key=lambda x: x.lower(), default=None)

        # Prepare the response
        response = {
            "is_success": True,
            "user_id": "shivansh_22bcs10784",
            "email": "22bcs10784@cuchd.in",
            "roll_number": "22BCS10784",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }

        return jsonify(response), 200
    except Exception as e:
        return handle_exception(e)

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    # Expected GET response body
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':

    app.run(debug=True)