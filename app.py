# importing the necessary dependencies
import os
import nltk
import praw as pr
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from DataPreprocessing.preprocessing import Preprocessing
from sklearn.feature_extraction.text import TfidfTransformer,TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:

            reddit = pr.Reddit(client_id=used yours,
                               client_secret=used yours,
                               user_agent=used yours,
                               username=uesd yours,
                               password=used yours)
            print(reddit.read_only)
            reddit.read_only = True
            url = (request.form['message'])
            print(url)
            submission = reddit.submission(url=url)
            title = submission.title
            p = Preprocessing(title)


            result = p.text_cleaning()
            print(result)
            filename = 'Logisticstitle.pickle'
            model = pickle.load(open(filename, 'rb'))
            value=model.predict([result])
            return render_template('results.html', message=value[0])


        except Exception as e:
            print('The Exception message is: ', e)
            return render_template('results.html', message=e)
    # return render_template('results.html')
    else:
        return render_template('index.html')


port = int(os.getenv('PORT'))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)



