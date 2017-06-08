# SOURCE : https://pythonspot.com/en/flask-and-great-looking-charts-using-chart-js/
# SOURCE : http://www.patricksoftwareblog.com/creating-charts-with-chart-js-in-a-flask-application/
# SOURCE : http://www.chartjs.org/docs/latest/ 


from flask import *

app=Flask(__name__)

@app.route('/')
def home():
	return "Go to <br> /linechart : for linechart <br> /barchart : for barchart <br> /piechart : for piechart <br> /radarchart : for radarchart"

@app.route('/linechart')
def line():
	legend="Monthly data"
	labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
	values=[10,9,12,6,2,5,7,6]
	return render_template("line.html",values=values,labels=labels,legend=legend)

@app.route('/barchart')
def bar():
	legend="Data"
	labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
	values=[10,9,12,6,2,5,7,6]
	return render_template("bar.html",values=values,labels=labels,legend=legend)

@app.route('/piechart')
def pie():
	labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
	values=[10,9,12,6,2,5,7,6]
	colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC" , "#FAFAAA"]
	return render_template("pieanddoughnut.html",st=zip(values,labels,colors))

@app.route('/radarchart')
def radar():
	labels=["DCS","DSD","AMMC","EEIM","DSP"]
	value1=[68,69,85,81,89]
	value2=[85,88,65,95,96]
	return render_template("radar.html",value1=value1,value2=value2,labels=labels)

@app.route('/polarchart')
def polar():
	labels=["DCS","DSD","AMMC","EEIM","DSP"]
	values=[60,60,81,84,82]
	return render_template("polar.html",labels=labels,values=values)

@app.route('/bubblechart')
def bubble():
	return render_template("bubble.html")

@app.route('/scatterchart')
def scatter():
	return render_template("scatter.html")

@app.route('/mixedchart')
def mixed():
	return render_template("mixed.html")

if __name__=="__main__":
	app.debug=True
	app.run(port=5000)