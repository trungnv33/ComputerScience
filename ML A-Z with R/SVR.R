#import dataset
dataset= read.csv("Position_Salaries.csv")
dataset= dataset[2:3]
library(e1071)
# Fit model SVR
regressor = svm(formula = Salary~., 
                data = dataset,
                type = 'eps-regression')
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

  