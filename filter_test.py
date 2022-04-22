# Source: https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/

import csv
import shutil
import os

file = open(r"E:\Diabetic Retinopathy\B. Disease Grading\B. Disease Grading\2. Groundtruths\test.csv")

csvreader = csv.reader(file)
header = next(csvreader)
header = header[:3]

print(header)
rows = []
for row in csvreader:
    row = row[:3]
    rows.append(row)
print(rows)

dib_ret_0, dib_ret_1, dib_ret_2, dib_ret_3, dib_ret_4 = ([] for i in range(5))

for img in rows:
    if (int(img[1]) == 0):
        dib_ret_0.append('/' + img[0] + '.jpg')
    elif (int(img[1]) == 1):
        dib_ret_1.append('/' + img[0] + '.jpg')
    elif (int(img[1]) == 2):
        dib_ret_2.append('/' + img[0] + '.jpg')
    elif (int(img[1]) == 3):
        dib_ret_3.append('/' + img[0] + '.jpg')
    else:
        dib_ret_4.append('/' + img[0] + '.jpg')

src = 'E:/Diabetic Retinopathy/B. Disease Grading/B. Disease Grading/1. Original Images/b. Testing Set/'
dest = 'E:/Diabetic Retinopathy/Test/'
dest_0 = dest + '0'
dest_1 = dest + '1'
dest_2 = dest + '2'
dest_3 = dest + '3'
dest_4 = dest + '4'

dest_positive = dest + 'Db_positive'

for i in dib_ret_0:
    shutil.copy(os.path.normpath(src + i), os.path.normpath(dest_0))

for i in dib_ret_1:
    shutil.copy(os.path.normpath(src + i), os.path.normpath(dest_positive))

for i in dib_ret_2:
    shutil.copy(os.path.normpath(src + i), os.path.normpath(dest_positive))

for i in dib_ret_3:
    shutil.copy(os.path.normpath(src + i), os.path.normpath(dest_positive))

for i in dib_ret_4:
    shutil.copy(os.path.normpath(src + i), os.path.normpath(dest_positive))

print(dib_ret_0)
print(dib_ret_1)
print(dib_ret_2)
print(dib_ret_3)
print(dib_ret_4)

file.close()
