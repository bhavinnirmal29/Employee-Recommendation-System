
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# In[2]
from sklearn.model_selection import train_test_split
# In[3]

from sklearn.metrics import accuracy_score
import seaborn as sns; sns.set()

#In[4]:
import sklearn
from sklearn.neighbors import KNeighborsClassifier

# In[5]:
from sklearn.cross_validation import train_test_split

# In[7]:
data1 = pd.read_csv("E:/DEGREE/PROJECT WORK/Implementation/Book1.csv")
data1.head(5)

# In[8]:
data1.shape

# In[10]:
data1.isnull().any()

# In[11]:
data1.fillna(1)

# In[12]:
from sklearn.model_selection import train_test_split
Y=data1[' Placed'].values
X=data1.drop(' Placed',axis=1).values
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=21)

# In[13]:
print(Y)
# In[14]:

print(X)

# In[15]:
x_train

# In[16]:
y_test
# In[17]:
x_test
# In[18]:
results=[]
names=[]
names1=[]

# In[19]:
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
# In[21]:
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(x_train,y_train)

# In[22]:
kfold=KFold(n_splits=10)
cv_results=cross_val_score(KNeighborsClassifier(),x_train,y_train,cv=kfold,scoring='accuracy')
results.append(cv_results)
names.append('KNN')
print("%s: %f (%f) "%('KNN',cv_results.mean(),cv_results.std()))

# In[23]:
from sklearn.naive_bayes import GaussianNB
kfold=KFold(n_splits=10)
cv_results=cross_val_score(GaussianNB(),x_train,y_train,cv=kfold,scoring='accuracy')
results.append(cv_results)
names.append('NB')
print("%s: %f (%f) "%('NB',cv_results.mean(),cv_results.std()))
# In[24]:
fig=plt.figure()
fig.suptitle('Comparison')
ax=fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

from sklearn.metrics import confusion_matrix

model=GaussianNB()
model.fit(x_train, y_train)
pred = model.predict(x_test)
mat = confusion_matrix(pred, y_test)
names = np.unique(pred)

sns.heatmap(mat, square=True, annot=True, fmt='d', cbar=False,xticklabels=names, yticklabels=names)
plt.xlabel('Truth')
plt.ylabel('Predicted')

model = KNeighborsClassifier()  

model.fit(x_train,y_train)


print('\nThe number of neighbors used to predict the target : ',model.n_neighbors)

predict_train = model.predict(x_train)
print('\nTarget on train data',predict_train) 

# Accuray Score on train dataset
accuracy_train = accuracy_score(y_train,predict_train)
print('accuracy_score on train dataset : ', accuracy_train)


predict_test = model.predict(x_test)
print('Target on test data',predict_test) 

# Accuracy Score on test dataset
accuracy_test = accuracy_score(y_test,predict_test)
print('accuracy_score on test dataset : ', accuracy_test)

