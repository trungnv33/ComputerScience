# Polynomial Regression
# import dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]
# Fitting linear model: 
lin_reg=  lm(formula = Salary~. ,  
             data = dataset)
summary(lin_reg)
# Fitting polynomial Regression:
dataset$Level2 = dataset$Level**2
dataset$Level3 = dataset$Level**3
dataset$Level4 = dataset$Level**4
lin_reg2 = lm(formula= Salary~., 
              data= dataset)
summary(lin_reg2)
# Visualize linear regression plot:
library(ggplot2)
ggplot() +
  geom_point(aes(x =dataset$Level ,y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x =dataset$Level ,y = predict(lin_reg, newdata= dataset)),
            colour = 'blue') +
  ggtitle('Linear Regression') +
  xlab("Level")+
  ylab("Salary")
# Visualize the poly Regression    
ggplot() +
  geom_point(aes(x =dataset$Level ,y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x =dataset$Level ,y = predict(lin_reg2, newdata= dataset)),
            colour = 'blue') +
  ggtitle('Polynomial Regression') +
  xlab("Level")+
  ylab("Salary")
# Predicting Linear Regression
y_pred = predict(lin_reg, newdata = data.frame(Level = 6.5))
# Predict Poly Regression
y_pred = predict(lin_reg2, newdata = data.frame(Level = 6.5,
                                                Level2 = 6.5**2,
                                                Level3 =6.5**3,
                                                Level4 = 6.5**4))

