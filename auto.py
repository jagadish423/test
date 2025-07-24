import pandas as pd

df = pd.read_csv('auto.csv')

# Show statistical details
print(df.describe())

# Get all cars with 8 cylinders
print(df[df['cylinders'] == 4])

# Number of cars per model year
print(df.groupby('model year').size().sort_index())
