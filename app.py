from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
def demo():
    return render_template('base.html')

@app.route('/login', methods =['GET'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
 app.run(debug=True)