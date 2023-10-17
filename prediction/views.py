from django.shortcuts import render

import pickle
import pandas as pd
import sklearn
from .models import Book_tbl, Prediction_tbl

def getPrediction(Edition, Reviews, Ratings, Edition_Year):
    model = pickle.load(open('prediction/model_grb.pkl', 'rb'))
    # scaled = pickle.load(open('scaler.pkl', 'rb'))
    # transform = scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]])
    dict_edit_rus = {"Твердый": 1, "Мягкий": 2, "Спиральный": 3, "Другой": 4}
    if Edition not in dict_edit_rus:
        Edition = "Другой"
    Edition = dict_edit_rus[Edition]
    transform = pd.DataFrame([[Edition, Reviews, Ratings, Edition_Year]], columns = ['Edition', 'Reviews', 'Ratings', 'Edition_Year'])
    prediction = model.predict(transform)
    print(' ===== prediction ====', prediction[0])
    return prediction[0]

def save_predict(Edition, Reviews, Ratings, Edition_Year, Price, user):
    dict_edit_rus = {"Твердый": 1, "Мягкий": 2, "Спиральный": 3, "Другой": 4}
    # pred = Prediction_tbl(Edition, Reviews, Ratings, Edition_Year, Price)
    # pred.save()
    pred = Prediction_tbl.objects.create(author=user, Edition=Edition, Reviews=Reviews, Ratings=Ratings,
                                         Edition_Year=Edition_Year, Price=Price)

def post_result(request):
    Edition = str(request.GET['edition'])
    Reviews = float(request.GET['reviews'])
    Ratings = int(request.GET['ratings'])
    Edition_Year = int(request.GET['year'])

    result_price = getPrediction(Edition, Reviews, Ratings, Edition_Year)
    save_predict(Edition, Reviews, Ratings, Edition_Year, round(result_price, 1), request.user)
    books = Prediction_tbl.objects.all().order_by('-created_on')[:30:1]
    return render(request, 'prediction/prediction_list.html', {'books': books})


def post_prediction(request):
    template_name = 'prediction/prediction.html'
    return render(request, template_name)

def show_books_tbl(request):
    books = Book_tbl.objects.all()[:30:1]
    return render(request, 'prediction/booklist.html', {'books': books})

def show_prediction_tbl(request):
    books = Prediction_tbl.objects.all().order_by('-created_on')[:30:1]
    return render(request, 'prediction/prediction_list.html', {'books': books})