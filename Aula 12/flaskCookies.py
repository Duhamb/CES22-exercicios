from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
	if request.method == 'POST':
		user = request.form['Name']
		p1g = request.form['p1']
		p2g = request.form['p2']
		exg = request.form['ex']
	
	resp = make_response(render_template('readcookie.html'))
	resp.set_cookie('userID', user)
	resp.set_cookie('p1g', p1g)
	resp.set_cookie('p2g', p2g)
	resp.set_cookie('exg', exg)

	return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>'+name+', your final grade is </h1>'

if __name__ == '__main__':
   app.run(debug = True)
