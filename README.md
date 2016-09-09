# linearregression
python module for linear regression by gradient descent, excercise for stanford machine learning course

To use;
from linear_regression import linreg
linreg.linear_regression(data,t0,t1,alpha,limit)

where
data is [(x1,y1),(x2,y2),,,(xi,yi)]
t0,t1 are initial guesses for theta0, theata1
alpha is the learning rate
limit is the limit for difference in loss for two consectutive iterations;  when difference<limit iteration stops and the resulting t0,t1 are returned
