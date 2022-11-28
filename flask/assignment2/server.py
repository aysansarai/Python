from secrets import choice
from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route("/")
def initial_render():
    return "Hello!"

@app.route('/play')                           
def route_play1():
    return render_template('index.html', number=3)  

@app.route('/play/<number_of_boxes>')                           
def route_play2(number_of_boxes):
    number= int(number_of_boxes)
    return render_template('index.html',number=number)  

@app.route('/play/<number_of_boxes>/<color>')                           
def route_play3(number_of_boxes, color):
    number= int(number_of_boxes)
    color_choice = color
    return render_template('index.html', number=number, color_choice=color_choice)  
    
if __name__=="__main__":
    app.run(debug=True)                   

