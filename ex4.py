from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Food, Western, Eastern, Asian, isFood')
pyDatalog.create_terms('French origin, Italian ogirin, isEastern')
pyDatalog.create_terms('Bread, isFrench')
pyDatalog.create_terms('Baguette, isBread')
pyDatalog.create_terms('isItalian')
pyDatalog.create_terms('Penne, hasSauce')


isEastern(X) <= hasSauce(X) & isItalian(X)
isEastern(X) <= isFrench(X)

+ isFood('Western')
+ isFood('Eastern')
+ isFood('Asian')

+ isFrench('Baguette')
+ isBread('Baguette')

+ hasSauce('Penne')
+ isItalian('Penne')

print("is eastern :",pyDatalog.ask('isEastern(X)').answers)
