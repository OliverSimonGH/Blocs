import os
from flask import Flask, redirect, request,render_template, jsonify

app = Flask(__name__)

# @app.route("/navbar_template", methods=['GET'])
# def navigation():
#     if request.method == 'GET':
#         return render_template('navbar.html')

if __name__ == "__main__":
    app.run(debug=True)
