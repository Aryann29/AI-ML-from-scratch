import numpy as np
class SimpleLinearRegression:

    #bestfit line y = mx+b 

    def __init__(self):
        self.m = None
        self.b = None
    
    def fit(self,x,y):
        x = np.array(x)
        y = np.array(y)
        
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        num = 0
        den = 0

        for i in range(len(x)):
            num += (x[i] - x_mean) * (y[i] - y_mean)
            den += (x[i] - x_mean) ** 2
        
        m = num / den 
        b = y_mean - m * x_mean

        self.m = m
        self.b = b

    def predict(self,x):
        return self.m * x + self.b


X = [1,2,3,4,5]
Y = [5,10,15,20,25]

myModel = SimpleLinearRegression() 
myModel.fit(X,Y)
print(myModel.predict(3))