dataset = read.csv('Salary_data.csv')
dataset
library(caTools)
set.seed(123)
# split training and test set
split=  sample.split(dataset$Salary,SplitRatio = 2/3)
training_set=  subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)
# FIT linear regression
regressor = lm(formula = Salary~ YearsExperience,data= training_set)
# predict test_set
y_pred = predict(regressor, newdata= test_set)
# visualize
library(ggplot2)
ggplot() +
  geom_point(aes(x= training_set$YearsExperience,y= training_set$Salary),
             colour = 'red') +
  geom_line(aes(x = training_set$YearsExperience,y = predict(regressor, newdata= training_set)),
            colour= 'blue') +
  ggtitle('Salary vs Experience (Training_set)') +
  xlab('Year of experience') + 
  ylab('Salary')

