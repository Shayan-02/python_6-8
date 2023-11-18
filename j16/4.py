import pandas as pd

# Define a dictionary
my_dict = {'key1': [1, 2, 3], 'key2': ['a', 'b', 'c']}

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(my_dict)

# Write the DataFrame to a text file (e.g., CSV)

df.to_csv('output.txt', sep='\t', index=False)
