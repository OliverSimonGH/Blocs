from flask import Flask, request, render_template

app = Flask(__name__, static_url_path="/static")

@app.route("/")
@app.route("/home")
def default():
    #return "Hello, world"
    return render_template('home.html')

@app.route("/navbar")
def navbar():
    return render_template('navbar.html')

if __name__ == "__main__":
    app.run(debug=True)
