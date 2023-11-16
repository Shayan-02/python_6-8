# dataset:
# 1) structural ---> excel, csv, txt, ...
# 2) unsctrucural ---> image, voice, text (email), ...

import pandas as pd

# student table
student_info = {
    "name" : ['amin', 'ali', 'reza', 'amir'],
    "age" : [20, 23, 21, 22],
    "degree" : ['BS', 'BS', 'MS', 'MS'],
    "ins" : [True, False, True, False],
    "gpa" : [3.5, 3.7, 3.6, 3.8]
}

for key, value in student_info.items():
    print(f"key: {key}\tvalue: {value}")

student_df = pd.DataFrame(student_info)
print(student_df)