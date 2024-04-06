
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('sf_clean.csv')

df = pd.DataFrame(df)

x = df[['sqft', 'beds', 'bath', 'hood_district']]
y = df[['price']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

mlr = LinearRegression()

mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)

