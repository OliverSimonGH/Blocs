from flask import Flask, request, render_template

app = Flask(__name__, static_url_path="/static")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/emails")
def emails():
    return render_template('emails.html')

@app.route("/logs")
def logs():
    return render_template('logs.html')

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/settings")
def settings():
    return render_template('settings.html')

@app.route("/nav")
def nav():
    return render_template('navbar.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
