from flask import Flask
from flask import request,render_template,redirect
import pickle
from werkzeug.utils import secure_filename
import os
import pandas as pd
from cleaner import main
from model import model
from nltk import word_tokenize

UPLOAD_FOLDER = '/home/walker/Desktop/innerchef/Predictor_App/uploads'
ALLOWED_EXTENSIONS = set(['csv','xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_filename(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/index",methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No File Part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No selected File')
			return redirect(request.url)
		if file and allowed_filename(file.filename):
			filename = secure_filename(file.filename)
			filename_tokenized = file.filename.split('.')
			if filename_tokenized[-1] == 'xlsx':
				data = pd.read_excel(file)
			else:
				data = pd.read_csv(file)
			#file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			print data.head(5)
			cleaned_data = main(data)
			print "Data is all Cleaned"
			print "\\\\"
			print "Going to Classify the Data"
			classified_dataframe = model(cleaned_data)

			classified_dataframe.to_csv(filename_tokenized[0]+".csv",index = False,encoding = 'utf-8')
			return render_template('final.html',title = 'All Done')								 							
	return render_template('index.html',title = 'Predictor_App | Home') 
	

if __name__ == '__main__':
	app.run(debug = True)	