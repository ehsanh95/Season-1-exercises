import numpy as np
import matplotlib.pyplot as plt

f = open("Files/project_data.csv" , "r" )
text=f.read()
f.close()
# print(text)

# داده را به صورت خط به خط جدا کردیم #
lines=text.split("\n")  
# print(lines)

# تشکیل یک لیست کلی که عصو های آن
#  لیست های متشکل از ستون هایی
#  استرینگ میباشند
table=[]        
for line in lines:
    if line:
        columns=line.split(",")
        table.append(columns)

#حذف خط اول که عنوان ستون ها هستند
table.pop(0)   
# print(table)

# خط به خط ستون های مورد نظر
#  را درون لیست دیگری میریزیم
values_columns=[]
for column in table:
    values_columns.append([int(column[1]),int(float(column[5]))])
values_columns.reverse() 
# print(values_columns)

values_array=np.array(values_columns)
values_close=values_array[:,1]
days=values_array[:,0]
days=days
print(days)
plt.plot(values_close)
plt.show()
