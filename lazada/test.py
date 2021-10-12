"""
    File để test chứ không còn tác dụng gì khác
"""
item = "9.350 ₫"
print(item)
check = item[-2::]
try:
    check = float(check)
except:
    item = item[0:-2]

print(check)
print(type(check))