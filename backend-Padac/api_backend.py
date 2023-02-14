from flask import Flask

app = Flask(__name__)

@app.route('/api/v1', methods=['GET'])
def hello_world():
    return 'Test'

if __name__ == '__main__':
    app.run(debug=True,port=8080)