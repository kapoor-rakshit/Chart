# SOURCE : https://pythonspot.com/en/flask-and-great-looking-charts-using-chart-js/
# SOURCE : http://www.patricksoftwareblog.com/creating-charts-with-chart-js-in-a-flask-application/
# SOURCE : http://www.chartjs.org/docs/latest/ 


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

@app.route('/barchart')
def bar():
	labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
	values=[10,9,12,6,2,5,7,6]
	return render_template("bar.html",values=values,labels=labels)

@app.route('/piechart')
def pie():
	labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]
	values=[10,9,12,6,2,5,7,6]
	colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC" , "#FAFAAA"]
	return render_template("pie.html",st=zip(values,labels,colors))

if __name__=="__main__":
	app.debug=True
	app.run(port=5000)