#----------------------------------------------------------------
# Cai dat va cap nhat thu vien
update.packages("tools")
install.packages("ggplot2", lib="C:\\Users\\lybuu\\Documents\\R\\win-library\\4.1")
update.packages("ggplot2")
update.packages("data.table")
library(data.table)
#----------------------------------------------------------------
setwd('E:\\dataLazada')
data = read.csv("LazData.csv", header=TRUE)
summary(data)   # Tong quan ve du lieu
View(data)
#----------------------------------------------------------------
