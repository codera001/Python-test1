#question 1.1
# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target (species) column to the dataframe
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the dataset
print(df.head())

# question 1.2
# Check data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

#question1.3
# If there are missing values (though in the Iris dataset there shouldn't be)
df.fillna(df.mean(), inplace=True)  # Replace missing values with the mean

#question 2.1
# Compute basic statistics for numerical columns
print(df.describe())

#question 2.2
# Grouping by 'species' and computing the mean for each numerical column
print(df.groupby('species').mean())


#question 3.1
# Line chart for petal length
plt.figure(figsize=(10,6))
plt.plot(df.index, df['petal length (cm)'])
plt.title('Petal Length over Index')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.show()

#question 3.2
# Bar chart for average petal length per species
plt.figure(figsize=(10,6))
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

#question 3.3
# Histogram for sepal length
plt.figure(figsize=(10,6))
df['sepal length (cm)'].hist(bins=20)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

#question 3.4
# Scatter plot for sepal length vs petal length
plt.figure(figsize=(10,6))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['species'].map({'setosa': 'r', 'versicolor': 'g', 'virginica': 'b'}))
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()


