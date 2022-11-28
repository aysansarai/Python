from secrets import choice
from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route("/")
def initial_render():
    return render_template('index.html',row=8,col=8, color0='red',color1='black')

@app.route("/<row>")
def render2(row):
    row=int(row)
    return render_template('index.html', row=row,col=8,color0='red',color1='black')

@app.route("/<row>/<col>")
def render3(row,col):
    row=int(row)
    col=int(col)
    return render_template('index.html', row=row,col=col,color0='red',color1='black')

@app.route("/<row>/<col>/<color0>")
def render4(row,col, color0):
    row=int(row)
    col=int(col)
    return render_template('index.html', row=row,col=col,color0=color0, color1='black')

@app.route("/<row>/<col>/<color0>/<color1>")
def render5(row,col,color0,color1):
    row=int(row)
    col=int(col)
    return render_template('index.html', row=row,col=col,color0=color0, color1=color1)

if __name__=="__main__":
    app.run(debug=True, port=5001)                   

