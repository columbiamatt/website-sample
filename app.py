from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/results')
def results():
	return render_template('results.html')

@app.route('/methodology')
def methodology():
	return render_template('methodology.html')

@app.route('/question')
def question():
	return render_template('question.html')

@app.route('/description')
def description():
	return render_template('description.html')

@app.route('/allegany')
def allegany():
	return render_template('allegany.html')

@app.route('/anne_arundel')
def anne_arundel():
	return render_template('anne_arundel.html')

@app.route('/baltimore_city')
def baltimore_city():
	return render_template('baltimore_city.html')

@app.route('/baltimore_county')
def baltimore_county():
	return render_template('baltimore_county.html')

@app.route('/calvert')
def calvert():
	return render_template('calvert.html')

@app.route('/caroline')
def caroline():
	return render_template('caroline.html')

@app.route('/carroll')
def carroll():
	return render_template('carroll.html')

@app.route('/cecil')
def cecil():
	return render_template('cecil.html')

@app.route('/charles')
def charles():
	return render_template('charles.html')

@app.route('/dorchester')
def dorchester():
	return render_template('dorchester.html')

@app.route('/frederick')
def frederick():
	return render_template('frederick.html')

@app.route('/garrett')
def garrett():
	return render_template('garrett.html')

@app.route('/harford')
def harford():
	return render_template('harford.html')

@app.route('/howard')
def howard():
	return render_template('howard.html')

@app.route('/kent')
def kent():
	return render_template('kent.html')

@app.route('/montgomery')
def montgomery():
	return render_template('montgomery.html')

@app.route('/prince_georges')
def prince_georges():
	return render_template('prince_georges.html')

@app.route('/queen_annes')
def queen_annes():
	return render_template('queen_annes.html')

@app.route('/somerset')
def somerset():
	return render_template('somerset.html')

@app.route('/st_marys')
def st_marys():
	return render_template('st_marys.html')

@app.route('/talbot')
def talbot():
	return render_template('talbot.html')

@app.route('/washington')
def washington():
	return render_template('washington.html')

@app.route('/wicomico')
def wicomico():
	return render_template('wicomico.html')

@app.route('/worcester')
def worcester():
	return render_template('worcester.html')

if __name__ == "__main__":
	app.run(debug=True)

