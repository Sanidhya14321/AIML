import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#Handling missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Remove duplicates
df = df.drop_duplicates()

#Filtering data
first_class = df[df["Pclass"] == 1]
print("First class passengers: ", first_class.head())

#Bar plot of survived passengers
survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind = "bar", color="skyblue")
plt.title("Survival Rate by Class")
plt.ylabel("Survival rate")
plt.xlabel("Class")
plt.show()