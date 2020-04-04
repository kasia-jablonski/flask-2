from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
# debug=true makes server auto reload on file changes. Should not be used for a production app
environment = 'development'
if environment == 'development':
    app.debug = True

@app.route('/hello')
def index():
    firstName = request.args.get('name', 'Nobody')
    greet = request.args.get('greet', 'Hello')
    print(request.args)

    if firstName:
        greeting = f"{greet}, {firstName}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(port=5000) 