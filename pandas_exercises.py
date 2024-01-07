#Gunda Esra Altınışık Karaca

##################################################
# Pandas Exercises
##################################################


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Task 1: Identify the Titanic dataset from the Seaborn library.
#########################################

df = sns.load_dataset("titanic")
df.head(30)

#########################################
# Task 2: Find the number of male and female passengers in the Titanic dataset described above.
# #########################################

df["sex"].value_counts()

#########################################
# Task 3: Find the number of unique values of each column.
#########################################

for col in df.columns:
    print({col: df[col].nunique()})

#########################################
# Task 4: Find the unique values of pclass variable.
#########################################

df["pclass"].unique()

#########################################
# Task 5: Find the number of unique values for the pclass ve parch variables
#########################################

df["pclass"].value_counts()
df["parch"].value_counts()


#########################################
# Task 6: Check the type of the embarked variable. Change its type to category. Check the type again.
#########################################

df["embarked"].dtypes
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtypes

#########################################
# Task 7: Show all the information of those whose embarked value is C.
#########################################

df[(df["embarked"] == "C")]

#########################################
# Task 8: Show all the information of those whose embarked value is not S.
#########################################

df[(df["embarked"] != "S")]

#########################################
# Task 9: Show all information for passengers who are women and under 30 years old.
#########################################

df[(df["age"] < 30) & (df["sex"] == "female")]

#########################################
# Show the information of passengers that the "fare" is over 500 or over 70 years old.
#########################################

df[((df["fare"] > 500) | (df["age"] > 70))]

#########################################
# Task 11: Find the sum of the null values in each variable.
#########################################

df.isnull().sum()

#########################################
# Task 12: Drop the who variable from the dataframe.
#########################################

df.drop("who", axis=1, inplace=True)


#########################################
# Task 13: Fill the empty values in the deck variable with the most recurring value (mode) of the deck variable.
#########################################

df["deck"].fillna(df["deck"].mode()[0], inplace=True)

#########################################
# Task 14: Fill in the empty values of the age variable with the median of the age variable.
#########################################

df["age"].fillna(df["age"].median(), inplace=True)
x = df["age"].median()

#########################################
# Task 15: Find the sum, count, mean values of the survived variable in the breakdown of the Pclass and Gender variables.
#########################################

df.groupby(["sex", "pclass"]).agg({"survived": ["sum", "mean", "count"]})

#########################################
# Task 16:  Write a function that will give 1 to those under the age of 30 and 0 to those equal to or above 30.
# Using the function you wrote, create a variable named age_flag in the titanic data set. (use apply and lambda structures)
#########################################

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))
df["age_flag"] = df["age"].apply(age_30)

#########################################
# Task 17: Define the Tips data set within the Seaborn library.
#########################################

df = sns.load_dataset("tips")
df.head()

#########################################
# Task 18: Find the sum, min, max and average of total_bill values according to the categories (Dinner, Lunch) of the Time variable.
#########################################

df.groupby("time").agg({"tip": ["min", "max", "mean"]})

#########################################
# Task 19: Find the sum, min, max and average of total_bill values according to days and time.
#########################################

df.groupby("time").agg({"tip": ["sum", "min", "max", "mean"]})


#########################################
# Task 20: Find the sum, min, max and average of the total_bill and type values of the lunch time and female customers according to the day.
#########################################

df[(df['sex'] == 'Female') & (df['time'] == 'Lunch')].groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean'], 'tip': ['sum', 'min', 'max', 'mean']})


#########################################
# Task 21: What is the average of orders with size less than 3 and total_bill greater than 10?
#########################################

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()


#########################################
# Task 22: Create a new variable called total_bill_tip_sum. Let it give the total bill and tip paid by each customer.
#########################################

df.head()
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]

#########################################
# Task 23: Sort from largest to smallest according to the total_bill_tip_sum variable and assign the first 30 people to a new dataframe.
#########################################

new_df = df.sort_values("total_bill_tip_sum", ascending=False)
new_df1 = new_df[:30]

df[["sex", "survived"]].groupby("sex")

