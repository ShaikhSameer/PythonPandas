import pandas as pd

df = pd.read_csv('data/sample_data_3.csv')
# print(df)


"""
#
#   findout how many schools we have
#
"""
num_schools = df['school_code'].nunique()
print(f"Number of schools: {num_schools}")


"""
#
#   find out the number of class we have in each school
#
"""

classes_per_school = df.groupby('school_code')['class'].nunique()
print("Number of classes in each school:")
print(classes_per_school)

"""
#
#   find out the avg, min and max age of students of each school.
#
"""

age_per_school = df.groupby('school_code')['age'].agg(['mean', 'min', 'max'])
print(age_per_school)


