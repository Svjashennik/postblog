from django.shortcuts import render

import pickle
import pandas as pd
import sklearn
from .models import Book_tbl, Prediction_tbl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn import metrics

def getPrediction(Edition, Reviews, Ratings, Edition_Year):
    model = pickle.load(open('prediction/model_grb.pkl', 'rb'))
    # scaled = pickle.load(open('scaler.pkl', 'rb'))
    # transform = scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]])
    dict_edit_rus = {"Твердый": 1, "Мягкий": 2, "Спиральный": 3, "Другой": 4}
    if Edition not in dict_edit_rus:
        Edition = "Другой"
    Edition = dict_edit_rus[Edition]
    transform = pd.DataFrame(
        [[Edition, Reviews, Ratings, Edition_Year]], columns=['Edition', 'Reviews', 'Ratings', 'Edition_Year']
    )
    prediction = model.predict(transform)
    return prediction[0]


def save_predict(Edition, Reviews, Ratings, Edition_Year, Price, user):
    dict_edit_rus = {"Твердый": 1, "Мягкий": 2, "Спиральный": 3, "Другой": 4}
    # pred = Prediction_tbl(Edition, Reviews, Ratings, Edition_Year, Price)
    # pred.save()
    pred = Prediction_tbl.objects.create(
        author=user, Edition=Edition, Reviews=Reviews, Ratings=Ratings, Edition_Year=Edition_Year, Price=Price
    )


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

def learn_model(request):
    def preprocess(data):
        data["Reviews"] = data["Reviews"].apply(lambda x: x.replace(" out of 5 stars", ""))
        data["Ratings"] = data["Ratings"].apply(
            lambda x: x.replace(" customer reviews", "").replace(" customer review", "").replace(",", ""))
        data["Genre"] = data["Genre"].apply(lambda x: x.strip('(Books)').strip('Textbooks'))
        data['Edition_Year'] = data['Edition'].apply(lambda x: x.split()[-1] if x.split()[-1].isdigit() else 0)
        data['Edition'] = [x.split(',')[0] for x in data['Edition']]
        data.loc[data['Genre'].value_counts()[data['Genre']].values < 10, 'Genre'] = "OtherGenre"
        return data

    def preprocess2(data):
        dict_edit = {'Paperback': 1, 'Hardcover': 2, 'Spiral-bound': 3}
        data['Edition_Year'] = data['Edition_Year'].apply(lambda x: x if x != 'na' else None)
        data['Edition'] = data['Edition'].apply(lambda x: dict_edit[x] if x in dict_edit else 4)
        return data

    # Считывание данных
    train_data = pd.read_excel('prediction/input/train.xlsx')
    test_data = pd.read_excel('prediction/input/test.xlsx')
    data = pd.concat([train_data, test_data])
    feature = data.drop([], axis=1)
    target = data[['Price']]

    pre_data = preprocess(feature)
    df = preprocess2(pre_data)

    df_min = df[['Edition', 'Reviews', 'Ratings', 'Edition_Year']]

    features_train = df_min[:6237]

    target = target.dropna(axis=0)

    X_train, X_val, Y_train, Y_val = train_test_split(features_train, target, test_size=0.25, random_state=42)

    gbr = GradientBoostingRegressor(learning_rate=0.003, max_depth=10,
                                    max_features='log2', min_samples_leaf=10,
                                    min_samples_split=7, n_estimators=1200)
    gbr.fit(X_train, Y_train)
    y_pred = gbr.predict(X_val)
    y_pred = y_pred.reshape(1560, 1)
    y_true = Y_val

    ### Вычисляем точность
    train_accuracy_score = gbr.score(X_train, Y_train)
    test_accuracy_score = gbr.score(X_val, Y_val)
    error = np.sqrt(np.square(np.log10(y_pred + 1) - np.log10(y_true + 1)).mean())
    score = round(float(1 - error) * 100, 1)
    r2_sc = round(float(metrics.r2_score(y_true, y_pred)) * 100, 1)
    mean_sq_log_er = round(float(metrics.mean_squared_log_error(y_true, y_pred)) * 100, 1)

    filename = 'model_grb_NEW.pkl'
    pickle.dump(gbr, open(filename, 'wb'))

    return render(request, 'prediction/model_metrics.html', {'sc1': score, 'file': filename})
