dataset = read.csv('Churn.csv')
dataset = dataset[,5:21]
dataset$Int.l.Plan =as.numeric(as.factor(dataset$Int.l.Plan))
dataset$VMail.Plan =as.numeric(as.factor(dataset$VMail.Plan))
dataset$Churn = factor(dataset$Churn,
                           levels= c('True.','False.'),
                           labels = c(1,0))
########### COrrelation ####
attach(dataset)
library(ggcorrplot)
corr =  cor(dataset[,1:16])
################Random Forest#############
#install.packages('randomForest')
library('randomForest')
library(caTools)
set.seed(123)
split=  sample.split(dataset,SplitRatio = 0.8)
training_set=  subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)
regressor = randomForest(Churn~.,data = training_set)
y_pred = predict(regressor,test_set)
y_pred_all = predict(regressor,dataset)
########## Confusion matrix###########
library(caret)
confusionMatrix(test_set$Churn,y_pred)
confusionMatrix(dataset$Churn,y_pred_all)
