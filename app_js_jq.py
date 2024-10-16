from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_jq.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    return f"<p>Hello, {name}! Thank you for submitting the form.</p>"

if __name__ == '__main__':
    app.run(debug=True)
