import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv('./dataset/train.csv')
test = pd.read_csv('./dataset/test.csv')
submission = pd.read_csv('./dataset/gender_submission.csv')

print(train.info())
print(train.describe())
print(train.head())
print(train.isnull().sum())

train = train.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)

train['Age'] = train['Age'].fillna(train['Age'].mean())
train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])

train['Pclass'] = train['Pclass'].astype('category')

surv_rate = train['Survived'].astype(int).mean()
print("Survival Rate:", surv_rate * 100)

surv_gender = train.groupby('Sex')['Survived'].mean()
print("Survival Rate by Gender:", surv_gender)

surv_class = train.groupby('Pclass')['Survived'].mean()
print("Survival Rate by Class:", surv_class)

age_corr = train[['Age', 'Survived']].corr()
print("Age & Survival Correlation:", age_corr)

plt.figure(figsize=(10, 5))
plt.bar(surv_gender.index, surv_gender.values, color=['blue', 'pink'])
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.show()

plt.figure(figsize=(10, 5))
plt.bar(surv_class.index.astype(str), surv_class.values,color=['gold', 'silver', 'brown'])
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Class')
plt.show()

plt.figure(figsize=(10, 5))
train[train['Survived'] == 1]['Age'].plot(kind='hist', bins=30, alpha=0.5, color='blue', label='Survived')
train[train['Survived'] == 0]['Age'].plot(kind='hist', bins=30, alpha=0.5, color='red', label='Did Not Survive')
plt.legend()
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
