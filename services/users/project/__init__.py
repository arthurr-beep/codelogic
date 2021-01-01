from flask import Flask, jsonify


#create an instance of the app
app = Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/hello', methods=['GET'])
def hello_hi():
    return jsonify({
        'status': 'success',
        'message': 'hi you!'
    })