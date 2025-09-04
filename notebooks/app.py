import sys
import pickle
#load the saved model

with open("models/logisticregression.pkl",'rb') as file:
  classifier=pickle.load(file)
#load the saved Vectrorizer
with open("models/countvectorizer.pkl",'rb') as file:
  vectorizer=pickle.load(file)
#load the saved encoder
with open("models/labelencoder.pkl",'rb') as file:
  encoder=pickle.load(file)

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os
if not os.path.exists('nltkdata'):
  os.mkdir('nltkdata')
  nltk.download('wordnet',download_dir='nltkdata')
  nltk.download('stopwords',download_dir='nltkdata')
  nltk.download('omw-1.4',download_dir='nltkdata')
  nltk.download('punkt_tab', download_dir='nltkdata')

nltk.data.path.append("nltkdata")

lemmatizer=WordNetLemmatizer()
w_tokenizer=nltk.tokenize.WhitespaceTokenizer()
stop=stopwords.words('english')

import re
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def preprocessing(text):
    # Apply preprocessing
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'@user', '', text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'[^\w\s]', '', text)

    text = [lemmatizer.lemmatize(y) for y in word_tokenize(text)]
    text = [item for item in text if item not in stop]
    text = " ".join(text)
    return text

def predict_result(text):
  text=preprocessing(text)
  vect=vectorizer.transform([text])
  pred=classifier.predict(vect)
  result=encoder.inverse_transform(pred)
  if result[0] == 'OFF':
    result[0] = 'Its an Offensive word'
  elif result[0] == 'NOT':
    result[0] = 'Its an Non Offensive word'
  return result[0]

text=sys.argv[1]
pred=predict_result(text)
print('prediction of "{}" is {}'.format(text,pred))
