# import dataset
dataset = read.csv('50_Startups.csv')
dataset
# Encoding categorical data
dataset$State = factor(dataset$State,
                         levels= c('New York','California','Florida'),
                         labels = c(1,2,3))
# Split data into training and test sets
library(caTools)
set.seed(123)
split=  sample.split(dataset$Profit,SplitRatio = 0.8)
training_set=  subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)
# Fitting the model multi_LR: 
regressor =  lm(formula = Profit~.,
                data= training_set)
summary(regressor)
# predict the results
y_pred = predict(regressor, newdata= test_set )
# Backward elimination
regressor =  lm(formula = Profit~R.D.Spend + Marketing.Spend,
                data= training_set)
summary(regressor)

