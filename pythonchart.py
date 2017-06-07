from flask import *

app=Flask(__name__)

@app.route('/')
def home():
	return "Go to <br> /linechart : for linechart <br> /barchart : for barchart <br> /piechart : for piechart"

@app.route('/linechart')
def line():
	legend="Monthly data"
	labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
	values=[10,9,12,6,2,5,7,6]
	return render_template("line.html",values=values,labels=labels,legend=legend)

if __name__=="__main__":
	app.debug=True
	app.run(port=5000)