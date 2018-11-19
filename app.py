from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    return "Hello Andela Code Camp"

@app.route('/home')
def home():
    title= "Andela Code Camp"
    application = {
    'heading': 'Andela Code Camp Flask Session',
    'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    }
    return render_template("app.html", name=title, application=application)



if __name__ == '__main__':
    app.run(debug=True)
