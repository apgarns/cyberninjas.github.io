from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Add your routes for handling requests from the frontend here

if __name__ == '__main__':
    app.run(debug=True)

import hashlib

app = Flask(__name__)

def sha256_encrypt(input_string):
    sha256_hash = hashlib.sha256()
    input_bytes = input_string.encode('utf-8')
    sha256_hash.update(input_bytes)
    encrypted_string = sha256_hash.hexdigest()
    return encrypted_string

@app.route("/", methods=["GET", "POST"])
def index():
    encrypted_input = ""

    if request.method == "POST":
        user_input = request.form["user_input"]
        encrypted_input = sha256_encrypt(user_input)

    return render_template("index.html", encrypted_input=encrypted_input)

if __name__ == "__main__":
    app.run(debug=True)
