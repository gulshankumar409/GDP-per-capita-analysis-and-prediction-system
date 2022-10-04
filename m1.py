import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score
from joblib import dump,load
df=pd.read_csv('Dummies_GDP.csv')
y = df['GDP ($ per capita)']
X = df.drop(['GDP ($ per capita)'], axis=1)
y3 = y
X3 = df.drop(["Pop. Density (per sq. mi.)",'GDP ($ per capita)', 'Arable (%)',
                        'Climate', 'Deathrate',"Industry","Service" ,], axis=1)
X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.2, random_state=101,shuffle=True)
Final_file_GBR = GradientBoostingRegressor(learning_rate=0.1, n_estimators=400)
Final_file_GBR.fit(X3, y3)
dump(Final_file_GBR,'GDP_per_capita_prediction.joblib')
predictor_GBR=load('GDP_per_capita_prediction.joblib')
pred=predictor_GBR.predict([[31056997.00,647500.00,0.00,23.06,163.07,36.00,3.20,0.22,87.65,46.60,0.38,1.00,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]])
print(pred)