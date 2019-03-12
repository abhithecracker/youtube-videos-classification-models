from sklearn.utils import shuffle
from nltk.corpus import stopwords
import string
import re
import pandas as pd
import os

class merge:

	def clean_data(text):
	    text = re.sub('<[^>]*>', '', text)
	    emoticons = re.findall('(?::|;|=)(?:-)',text)
	    text = (re.sub('[\W]+', ' ', text.lower()) +
	            ' '.join(emoticons).replace('-', ''))
	    text = text.replace("b ","")
	    text = text.replace("n ","")
	    stop_words = stopwords.words('english')
	    rm_words = [w for w in text.split() if w.lower() not in stop_words]
	    return ' '.join(rm_words)
	    return text

	def prepare_data(self):

		# Declare path for Data
		path = 'data/'

		# check for the merged file and delete if already there
		if 'Youtube_data.csv' in os.listdir(path):
		    os.remove('data/Youtube_data.csv')

		# Create empty dataframe    
		data = pd.DataFrame()

		# Read the files in directory and append to single dataframe
		for file in os.listdir(path):
		    df = pd.read_csv(os.path.join(path,file))
		    data = data.append(df,ignore_index=True)

		# Shuffle Data
		data = shuffle(data)

		# Get stopwords
		stop_words = stopwords.words('english')

		# Clean Data
		data['Title'] = data['Title'].apply(self.clean_data)
		data['Description'] = data['Description'].apply(self.clean_data)
		data['Video Id'] = data['Video Id'].apply(self.clean_data)

		#save to CSV
		data.to_csv('data/Youtube_data.csv',index=False)




		    
