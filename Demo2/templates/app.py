from flask import Flask, render_template, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        encrypted_input = hashlib.sha256(user_input.encode('utf-8')).hexdigest()
        return jsonify(encrypted_input=encrypted_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
