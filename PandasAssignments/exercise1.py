import pandas as pd

exam_data = pd.read_csv('data/exam.csv')

# print(exam_data)


"""
#
#   Get first three rows
#
"""

first_three_rows = exam_data.head(3)
print(first_three_rows)

"""
#
#   Get 'name' & 'score' columns
#
"""

sel_col = exam_data[['name', 'score']]
print(sel_col)

"""
#
# Get data from loc and iloc
#
"""

selected_data_loc = exam_data.loc[[1, 3], ['name', 'score']]

selected_data_iloc = exam_data.iloc[[1, 3], [0, 1]]  

print("Using loc:")
print(selected_data_loc)

print("\nUsing iloc:")
print(selected_data_iloc)

"""
#
#   select the rows where the number of attempts in the examination is greater than 2
#
"""

selected_rows = exam_data[exam_data['attempts'] > 2]
print(selected_rows)

"""
#
#   count the number of rows and columns 
#
"""

num_rows, num_columns = exam_data.shape
print(f"Number of rows: {num_rows}, Number of columns: {num_columns}")


"""
#
#   select the rows where the score is missing
#
"""

missing_score_rows = exam_data[exam_data['score'].isnull()]
print(missing_score_rows)


"""
#
#   select the rows the score is between 15 and 20
#
"""

selected_rows = exam_data[(exam_data['score'] >= 15) & (exam_data['score'] <= 20)]
print(selected_rows)


"""
#
#   select the rows where number of attempts in the examination is less than 2 and score greater than 15.
#
"""

selected_rows = exam_data[(exam_data['attempts'] < 2) & (exam_data['score'] > 15)]

print(selected_rows)


"""
#
#   change the score in row 'd' to 11.5
#
"""
exam_data.at[3, 'score'] = 11.5

print(exam_data)

"""
#
#   calculate the sum of the examination attempts by the students.
#
"""

sum_attempts = exam_data['attempts'].sum()

print(f"Sum of examination attempts: {sum_attempts}")


"""
#
#   calculate the mean of all students' scores
#
"""

mean_score = exam_data['score'].mean()

print(f"Mean of all students' scores: {mean_score}")


"""
#
#   sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order.
#
"""

sorted_exam_data = exam_data.sort_values(by=['name', 'score'], ascending=[False, True])

print(sorted_exam_data)


"""
#
#   replace the 'qualify' column contains the values 'yes' and 'no' with True and False.
#
"""

exam_data['qualify'] = exam_data['qualify'].map({'yes': True, 'no': False})

print(exam_data)

"""
#
#   change the name 'James' to 'Suresh' in name column.
#
"""

exam_data.loc[exam_data['name'] == 'James', 'name'] = 'Suresh'

print(exam_data)

"""
#
#   delete the 'attempts' column
#
"""

exam_data = exam_data.drop(columns=['attempts'])

print(exam_data)


"""
#
#   insert a new column
#
"""

exam_data['result'] = 'Pass'

print(exam_data)


"""
#
#   iterate over rows
#
"""

# for index, row in exam_data.iterrows():
#     print(f"Index: {index}, Name: {row['name']}, Score: {row['score']}, Attempts: {row['attempts']}, Qualify: {row['qualify']}")

"""
#
#   Display all columns
#
"""

all_columns = exam_data.columns
print(all_columns)

"""
#
#   Rename Column
#
"""

exam_data = exam_data.rename(columns={'name': 'std_names'})

print(exam_data)


"""
#
#    replace all the NaN values with Zero's in a column
#
"""

exam_data['score'] = exam_data['score'].fillna(0)

print(exam_data)


"""
#
#   Remove duplicates
#
"""

exam_data_no_duplicates = exam_data.drop_duplicates()

print(exam_data_no_duplicates)

"""
#
#   Drop multiple columns
#
"""

columns_to_drop = ['result', 'qualify']
exam_data = exam_data.drop(columns=columns_to_drop)

print(exam_data)


"""
#
#   Drop rows and then reset the index
#
"""

rows_to_drop = [0, 2]
exam_data = exam_data.drop(index=rows_to_drop)

exam_data = exam_data.reset_index(drop=True)

print(exam_data)

