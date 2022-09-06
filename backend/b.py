from flask import Flask

app = Flask(__name__)

@app.route("/name/<string:a>")
def he(a):
    return str(a)

if __name__=="__main__":
    app.run(debug=True)