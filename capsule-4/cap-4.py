import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

#pd.set_option('display.max_rows', None)
#pd.set_option('dispaly.max_columns', None)
#print(df.info())
#print(df.shape)
#print(df.columns)
unique_counts = df.nunique()
#print(unique_counts)

""" survived_values = df['survived'].unique()
print(survived_values)
print(f'survived column has {survived_values} unique values.')

sex_unique_values = df['sex'].unique()
print(sex_unique_values)
print(f'sex column has {sex_unique_values} unique values.')

#value_counts()
gender_value_count = df['sex'].value_counts()
print(gender_value_count)

survived_value_count = df['survived'].value_counts()
print(survived_value_count)

#group_by
grouped_data = df.groupby(['sex', 'survived'])['survived'].count()
print(grouped_data)

#survival by passenger class
survival_grouped = df.groupby(['pclass', 'survived'])['survived'].count()
print(survival_grouped)

embarked_class_survived_count = df.groupby(['embark_town', 'pclass', 'survived'])['survived'].count()
print(embarked_class_survived_count) """

#Use of seaborn
""" sns.countplot(x="sex", hue="survived", data=df)
plt.xlabel("Gender")
plt.ylabel("number of passengers")
plt.title("Survival by gender")
plt.show() """

""" sns.countplot(x="pclass", hue="survived", data=df)
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.title("Survival by Passenger class")
plt.show() """
#Plotting with catplot
""" sns.catplot(x="embark_town", hue="survived", col="pclass", data=df, kind="count", palette="Set2")
plt.xlabel("Embarkation town")
plt.ylabel("Number of passengers")
plt.suptitle("Survival by embarkation town and passenger classes")
plt.show() """

#Describe function
""" print(df['embark_town'].describe()) """

#Dropping columns
""" print(df['survived'].value_counts())
print(df['alive'].value_counts())

df.drop(columns=['alive'], inplace=True)

print(df.columns) """

""" print(df['embarked'].value_counts())
print(df['embark_town'].value_counts())

df.drop(columns="embarked", inplace=True)
print(df.columns) """

""" print(df['class'].value_counts())
print(df['pclass'].value_counts())

df.drop(columns=['class'], inplace=True)
 """
""" print(df['adult_male'].value_counts())

df['adult_male'].replace({True: 1, False: 0}, inplace=True)
print(df['adult_male'].value_counts()) """

""" print(df.isnull().sum()) """

sns.boxplot(y='age', data=df)
plt.title('Box plot of age column')
plt.show()

#imputing missing values
df['age'] = df['age'].fillna(df['age'].median())


#Deck col(688 missing values)
#Replacing missing with most frequent value
df['deck'] = df['deck'].fillna(df['deck'].mode()[0])


#embark_town
#dropping is better
df.dropna(subset=['embark_town'], inplace=True)

print(df.isnull().sum())

df.rename(columns={'deck':'cabin'}, inplace=True)

plt.hist(df['who'], color='skyblue', edgecolor='black')
plt.xlabel('Passenger Type')
plt.ylabel('Frequency')
plt.title('Distribution of passenger type')
plt.show()

numeric_df = df.select_dtypes(include=['int64', 'float64'])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='PuBuGn', fmt=".2f")
plt.title('Correlation Matrix of Titanic Dataset')
plt.show()