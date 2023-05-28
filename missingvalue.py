#import libary pandas
import pandas as pd

# membaca file csv yang telah didrop pada pycharm dengan read_csv
cd = pd.read_csv('shopping_data_missingvalue.csv')
# print('csv shopping data missing value') #untuk memanggil variabel cd
# print(cd)

# mencari jumlah data yang valuenya null
colum_null= cd.isnull()
# print(colum_null.sum())

# # mengisi value yang null

#column  Age
rata_umur = cd['Age'].mean()
cd['Age'] = cd['Age'].fillna(rata_umur)

#column Annual Income
income = cd['Annual Income (k$)'].mean()
cd['Annual Income (k$)'] = cd ['Annual Income (k$)'].fillna(income)

#column Spending score
score = cd['Spending Score (1-100)'].median()
cd['Spending Score (1-100)'] = cd['Spending Score (1-100)'].fillna(score)
#
print(cd)
