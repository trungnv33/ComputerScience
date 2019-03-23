require(ISLR)
require(MASS)
?lda
lda.fit = lda(Direction~Lag1+Lag2,data= Smarket,subset = Year== 2005)
plot(lda.fit)
fix(Smarket)
