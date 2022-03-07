from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    result = {
        'message': 'Hello World  tuần yêu dấu đến  đây',
        'status': 'Success'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000,host="0.0.0.0",debug=True)