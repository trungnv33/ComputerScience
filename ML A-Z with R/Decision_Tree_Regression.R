#import dataset
dataset= read.csv("Position_Salaries.csv")
dataset= dataset[2:3]
install.packages('rpart')
library(rpart)
# Fit model SVR
regressor = rpart(formula = Salary~., 
                data = dataset,
                control= rpart.control(minsplit= 1))
summary(regressor)
y_pred=  predict(regressor, newdata= data.frame(Level=  6.5))
##Visualize 
library(ggplot2)
ggplot()+ 
  geom_point(aes(x= dataset$Level,y=dataset$Salary),
             colour = 'red')+
  geom_line(aes(x= dataset$Level),y = predict(regressor,newdata=dataset),
            colour=  'blue')+
  ggtitle('SVR')+
  xlab('Level')+
  ylab('Salary')

