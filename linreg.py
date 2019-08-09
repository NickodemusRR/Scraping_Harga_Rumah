import pandas as pd             
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# melakukan linear regression pada data csv
# file rumah csv merupakan hasil beberapa kali webscraping untuk mendapatkan berbagai data rumah
myData = pd.read_csv('rumah.csv', index_col=0)
myData['harga'] = myData['harga'].apply(lambda x: x * (10 ** (-6))) # mengubah harga menjadi juta rupiah
# print(myData)

# split datasets: 90% training data & 10% test_data
x_train, x_test, y_train, y_test = train_test_split(
    myData[['luas']],
    myData['harga'],
    test_size = .1
)

# linear regression
model = LinearRegression()

# training
model.fit(x_train, y_train)

# slope/gradient/m best fit line:
# print(model.coef_[0])

# intercept/b best fit line:
# print(model.intercept_)

# plot best fit line
# y = mx + b
plt.plot(
    myData['luas'],
    model.coef_[0] * myData['luas'] + model.intercept_,
    'r-'
)

# plot dataframe
plt.scatter(
    myData['luas'],
    myData['harga'],
    marker='o',
    color='blue'
)

plt.title('Harga Rumah vs Luas Bangunan')
plt.xlabel('Luas (m2)')
plt.ylabel('Harga (juta rupiah)')
plt.grid(True)
plt.show()

# prediksi harga terbaik
print('Prediksi harga rumah dengan luas bangunan 65m2:', model.predict([[65]]))
print('Prediksi harga rumah dengan luas bangunan 100m2:', model.predict([[100]]))
print('Prediksi harga rumah dengan luas bangunan 200m2:', model.predict([[200]]))