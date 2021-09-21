from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/user_data', methods=['GET'])
def user_data():
    return ("Hello world"), 200


if __name__ == "__main__":
    app.run(debug=True)
