import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

# Heres what return does https://www.codecademy.com/en/forum_questions/51c0e35d7c82caace80008b1
def get_data(filename):
    with open(filename, 'r') as csvfile:
        print "Opened File"
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    print "Reading done"
    return

def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    print "Training lin"
    svr_lin.fit(dates, prices)
    print "Training poly"
    svr_poly.fit(dates, prices)
    print "Training rbf"
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    print "Predicting rbf"
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    print "Predicting lin"
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    print "Predicting poly"
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    print "Done"
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


get_data("/home/me/Downloads/aapl.csv")

predictedprice = predict_prices(dates, prices, 29)

print predictedprice