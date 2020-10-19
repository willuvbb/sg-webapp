from flask import Flask, render_template, request, jsonify

# A test app.
app = Flask(__name__)


@app.route('/')
def home():

    return render_template('Index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=82)


