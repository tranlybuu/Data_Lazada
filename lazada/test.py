"""
    File này dùng để test chứ không còn chức năng gì khác
"""

import os
import pandas as pd
import statistics as sta
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

"""
path = os.getcwd() + "\lazada"
os.chdir(path)


file = open('url.txt', 'r', encoding='UTF-8')
url_list = file.readlines()
file.close()

print(len(url_list))
"""

# arr_test = [4,6,2,3,1,8]
# print(arr_test.index(1))

data_check = data["p_brand"]
quantity_list_check = []
brand_list_check = []
for item in data_check:
    if item not in brand_list_check:
        brand_list_check.append(item)
        quantity_list_check.append(1)
    else:
        index = brand_list_check.index(item)
        quantity_list_check[index] = quantity_list_check[index]+1
quantity = []
brand = []
for item in range(len(quantity_list_check)):
    count = quantity_list_check[item]
    name_brand = brand_list_check[item]
    if count<10:
        name_brand = "Small-brand"
    
    if name_brand not in brand:
        brand.append(name_brand)
        quantity.append(count)
    else:
        index = brand.index(name_brand)
        quantity[index] = quantity[index] + count

brand_df = pd.Series(quantity, index=brand) # Tạo dataframe với 2 cột là tên danh mục và phần trăm các khoảng tiền
print(brand_df)
mylabels = brand_df.index
fig = plt.figure(figsize = (4, 4))
plt.title('Các thương hiệu sản phẩm', fontsize = 20, color = 'red')
sns.barplot(brand_df, mylabels, orient = 'h')