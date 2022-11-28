# MISSING SENSEI BONUS

from flask import Flask

app = Flask(__name__)

# Pass the required route to the decorator.
@app.route("/")
def hello_world():
	return "Hello, World!"
	
@app.route("/dojo")
def index():
	return "Dojo!"

@app.route('/say/<string:name>') 
def hello(name):
    print(name)
    return "Hi " + name.capitalize() + "!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
	# return (name.capitalize() + "\n") * num
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

if __name__ == "__main__":
	app.run(debug=True)
