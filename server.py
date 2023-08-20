from flask import Flask,request,jsonify,make_response

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json
    a=data['first']
    b=data['second']
    result=a+b
    response_data={'result': result}
    response= make_response(jsonify(response_data), 200)
    return response
    

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json
    a=data['first']
    b=data['second']
    result=a-b
    response_data={'result': result}
    response= make_response(jsonify(response_data), 200)
    return response

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
