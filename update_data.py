"""
    Đây là file để chỉnh sửa dữ liệu và xuất ra file csv mới
"""

import os
import pandas as pd

path = os.getcwd() + "\lazada"
os.chdir(path)

data_all_csv = []
all_folders = os.listdir(path)
for item in all_folders:
    if ".csv" in item:
        # bfile là file csv chứa dữ liệu trước khi chỉnh sửa 
        bfile = open(item, 'r', encoding='UTF-8')
        b_header = bfile.readline()
        product = bfile.readlines()
        bfile.close()
        data_all_csv.append(product)

path = path[:-7]
os.chdir(path)

# afile là file csv chứa dữ liệu trước khi chỉnh sửa 
afile = open('LazData.csv', 'a+', encoding='UTF-8')
afile.close()

check_data = pd.read_csv("LazData.csv")
name_product = check_data["p_name"]

for product in data_all_csv:
    for data in product:
        index_comma = []
        for x in range(len(data)):
            if data[x] == ",":
                index_comma.append(x)
        if len(index_comma) != 16:
            data = str(data[:(index_comma[3]+1)] + data[(index_comma[3]+1):index_comma[-12]].replace(",", " ") + data[index_comma[-12]:])
        data = data.replace("\n","").split(",")
        
        """ Xử lý tên sản phẩm """
        name = data[4]
        data[4].strip(" ").strip('"').strip("'")
        if "(" in name:
            a1 = name.index("(")
            a2 = name.index(")")
            data[4] = data[4].replace(data[4][a1:(a2+1)], "")
        if "[" in name:
            a1 = name.index("[")
            a2 = name.index("]")
            data[4] = data[4].replace(data[4][a1:(a2+1)], "")

        """ Xử lý giá sản phẩm: Xóa đơn vị tiền tệ và dấu phẩy -> kết quả trả về là số nguyên """
        if "." in data[6]:
            data[6] = data[6].replace(".","")
        if "₫" in data[6]:
            data[6] = data[6].replace("₫","")
        data[6] = data[6].strip()

        """ Xử lý số lượt đánh giá cho sản phẩm: Kết quả trả về chỉ là số nguyên """
        if ("Không có" in data[5]):
            data[5] = 0
        else:
            data[5] = data[5].split(" ")[0]

        """ Xử lý đánh giá trung bình: Chuyển về tỉ lệ % """
        if data[12] != "":
            data[12] = int(float(data[12])*20//1)
        else:
            data[12] = "##"

        """ Xử lý số lượng đánh giá từ 1->5 sao: Mất dữ liệu """
        try:
            data[7] = int(data[7])
            data[8] = int(data[8])
            data[9] = int(data[9])
            data[10] = int(data[10])
            data[11] = int(data[11])
        except:
            data[7] = "##"
            data[8] = "##"
            data[9] = "##"
            data[10] = "##"
            data[11] = "##"

        """ Xử lý tỉ lệ đánh giá của shop: Mất dữ liệu """
        if len(data[14])==0:
            data[14] = "##"
        else:
            data[14] = data[14].replace("%", "")

        """ Xử lý tỉ lệ phản hồi của shop: """
        if data[15]=="Không đủ thông tin" or data[15]=="not enough data":
            data[15] = "---"
        else:
            data[15] = data[15].replace("%", "")
        
        """ Xử lý tỉ lệ giao hàng của shop: """
        if data[16]=="Không đủ thông tin" or data[16]=="not enough data":
            data[16] = "---"
        else:
            data[16] = data[16].replace("%", "")


        #########################################################
        new_data = ""
        for item in data:
            new_data = new_data + str(item) + "~"
        new_data = new_data.strip("~").replace("~", ",") + "\n"

        if (data[4] not in name_product) and ("##" not in new_data):
            # afile là file csv chứa dữ liệu trước khi chỉnh sửa 
            afile = open('LazData.csv', 'a+', encoding='UTF-8')
            header = afile.readline()
            afile.write(new_data)
            afile.close()

        #0p_brand,1p_cate,2p_image,3p_mall,4p_name,5p_number_reviews,6p_price,7p_rate1star,8p_rate2star,9p_rate3star
        #10p_rate4star,11p_rate5star,12p_rating,13s_name,14s_rating,15s_response_rate,16s_ship_ontime
