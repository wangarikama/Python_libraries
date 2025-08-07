import pandas as pd

#create a DataFrame with some sample data
data = {
    'Name': ['Kamau', 'Stephen', 'Chris'],
    'Age': [15, 18, 20],
    'Grade': ['80', '45', '68']  # Note: Grades are strings
}
df = pd.DataFrame(data)

#Add new column "Passed"
df['Passed'] = df['Grade'].astype(int) >= 50

#filter and display students who passed equals to true
passed_students = df[df['Passed'] == True]

print(passed_students) 