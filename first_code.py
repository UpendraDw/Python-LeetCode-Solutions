import pandas as pd 
my_dict = {'FName':pd.Series(data = ['Upendra','Vivek','Abhishek']),'LName':pd.Series(['Dwivedi','Kumar','Sharma']),'Branch':pd.Series(['Electrical','Electrical'])}
df = pd.DataFrame(data = my_dict)
print(df)