from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "wlc to home page"
@app.route("/index")
def index():
    return "wlc to index"

if __name__=="__main__":
    app.run(debug=True)