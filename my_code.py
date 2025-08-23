import pandas as pd
import os

data = {
    'Name':["Aman","Rishi","James"],
    'Age':[23,25,27],
    'Score':[91,82,89]
}

df = pd.DataFrame(data)
# print(df)
# data is string of the folder name to be created
data_dir = 'data'
print(data_dir)

#used to make directory at root level
os.makedirs(data_dir,exist_ok=True)

# adding the file path for our data.csv file
file_path = os.path.join(data_dir,'sample.csv')

#index is false which means excluding Serial nos
df.to_csv(file_path,index=False)
print(df)