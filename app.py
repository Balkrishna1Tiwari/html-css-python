from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world!"


@app.route('/test_fun')

def how():
    a=89+89

    return 'this {a} is a combination of two numbers'.format(a)


if __name__=="__main__":
    app.run(host="0.0.0.0")