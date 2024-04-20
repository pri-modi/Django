from django.shortcuts import render
from .forms import detectionForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import detection
from .serializers import detectionSerializers
import pickle
import joblib
# from sklearn.externals import joblib
from sklearn.utils import _joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict, Counter
from nltk.util import pr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import string
import re
import nltk
stemmer = nltk.SnowballStemmer("english")
from nltk.corpus import stopwords

stopword=set(stopwords.words('english'))


# Create your views here.
class detectionView(viewsets.ModelViewSet):
    queryset = detection.objects.all()
    serializer_class = detectionSerializers



def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopword]
    text = " ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text = " ".join(text)
    return text






# @api_view(["POST"])
def detecting(text):
    try:
        cv = CountVectorizer()
        data = pd.read_csv("D:/Django/hateSpeech/MyAPI/twitter.csv")

        data["labels"] = data["class"].map({0: "Hate Speech",
                                            1: "Offensive Language",
                                            2: "Nor Hate neither offensive"})

        data = data[["tweet", "labels"]]
        data["tweet"] = data["tweet"].apply(clean)
        x = np.array(data["tweet"])
        y = np.array(data["labels"])
        X = cv.fit_transform(x)  # Fit the Data

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        clf = DecisionTreeClassifier()
        clf.fit(X_train, y_train)

        # sample = "Let's unite and kill all the people who are protesting against the government"
        sample_cleaned = clean(text)
        sample_vectorized = cv.transform([sample_cleaned]).toarray()
        prediction = clf.predict(sample_vectorized)
        return  ("Sample Prediction:", prediction)

        # mdl = joblib.load("D:\Django\hateSpeech\MyAPI\SD.pkl")

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def xyz(request):
    if request.method == 'POST':
        form = detectionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            myDict = (request.POST).dict()
            df = pd.DataFrame(myDict, index = [0])
            print(detecting(df))

    form = detectionForm()
    return render(request, 'myform/cxform.html', {'form': form})






#Cleaning text in tweets






