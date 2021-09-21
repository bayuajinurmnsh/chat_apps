from flask import Flask, request, jsonify, make_response
from datetime import datetime
import operations as ops

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_all_user():
    data = ops.get_users()
    return jsonify({'users': data}), 200


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    created_date = datetime.now()

    # check if data is valid or not
    valid_data = ops.valid_user_data(data)
    if valid_data:
        insert_data = ops.register(data, created_date)

        if insert_data == 'exists':
            return jsonify({'message': 'Username Already Exists', 'status': 'failed'}), 500

        if insert_data == False:
            return jsonify({'message': 'Failed to Insert Data', 'status': 'failed'}), 500

        return jsonify({'message': 'Data has been insert', 'status': 'success'}), 200

    else:
        return jsonify({'message': 'Data not valid', 'status': 'invalid'}), 500


if __name__ == "__main__":
    app.run(debug=True)
