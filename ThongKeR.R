#----------------------------------------------------------------
# Them thu vien
library(tidyverse)
library(plotly)
library(ggplot2)
library(dplyr)
#----------------------------------------------------------------
data = read.csv("https://raw.githubusercontent.com/tranlybuu/Data_Lazada/master/LazData.csv", encoding = "UTF-8", header = TRUE)
names(data)
str(data)
#----------------------------------------------------------------
# Tính mode
mode <- function (x, method = "mode", na.rm = FALSE)
{
  x <- unlist(x)
  if (na.rm)
    x <- x[!is.na(x)]
  u <- unique(x)
  n <- length(u)
  frequencies <- rep(0, n)
  for (i in seq_len(n)) {
    if (is.na(u[i])) {
      frequencies[i] <- sum(is.na(x))
    }
    else {
      frequencies[i] <- sum(x == u[i], na.rm = TRUE)
    }
  }
  if (method == "mode" | is.na(method) | method == "")
  {return(ifelse(length(frequencies[frequencies==max(frequencies)])>1,NA,u[which.max(frequencies)]))}
  
  if(method == "nmode" | method == "nmodes")
  {return(length(frequencies[frequencies==max(frequencies)]))}
  
  if (method == "modes" | method == "modevalues")
  {return(u[which(frequencies==max(frequencies), arr.ind = FALSE, useNames = FALSE)])}
  return()
}
# Mô t??? d??? li???u
describe <- function(x)
{
  av <- mean(x)
  tv <- median(x)
  sd <- sd(x)
  se <- sd/sqrt(length(x))
  min <- min(x)
  max <- max(x)
  c(MEAN=av, MEDIAN=tv, SD=sd, STD=se, MIN=min, MAX=max)
} 
#----------------------------------------------------------------
# Thuong hi???u
mode(data$p_brand)
describe(data$p_brand)
qplot(data$p_brand,xlab = "Thuong hi???u", ylab = "S??? lu???ng", main = "Bi???u d??? s??? lu???ng s???n ph???m c???a m???i thuong hi???u")
#---------------------------------------------------------------
# Danh m???c s???n ph???m
mode(data$p_cate)
describe(data$p_cate)
qplot(data$p_cate, xlab = 'Danh m???c', ylab = 'S??? lu???ng s???n ph???m', main = 'Bi???u d??? danh m???c s???n ph???m')
#----------------------------------------------------------------
# S???n ph???m chính hãng ho???c không chính hãng
mode(data$p_mall)
describe(data$p_mall)
qplot(data$p_mall, xlab = 'S???n ph???m chính hãng và không chính hãng', ylab = 'S??? lu???ng', main = 'Bi???u d??? s??? lu???ng LazMall và NonMall')
#----------------------------------------------------------------
# T???ng s??? lu???t dánh giá cho m???i s???n ph???m
mode(data$p_number_reviews)
describe(data$p_number_reviews)
hist(data$p_number_reviews,col = 'green',breaks=40,xlab = "S??? dánh giá cho m???i s???n ph???m", ylab = "S??? lu???ng", main = "Bi???u d??? th??? hi???n s??? dánh giá cho m???i s???n ph???m")
#----------------------------------------------------------------
# Giá c???a s???n ph???m
mode(data$p_price)
describe(data$p_price)
hist(data$p_price,col = 'pink',breaks=60,xlab = "S??? dánh giá cho m???i s???n ph???m", ylab = "S??? lu???ng", main = "Bi???u d??? th??? hi???n s??? dánh giá cho m???i s???n ph???m")
#----------------------------------------------------------------
# T???ng s??? lu???t dánh giá 1->5 sao cho m???i s???n ph???m
mode(data$p_rate1star)
describe(data$p_rate1star)
mode(data$p_rate2star)
describe(data$p_rate2star)
mode(data$p_rate3star)
describe(data$p_rate3star)
mode(data$p_rate4star)
describe(data$p_rate4star)
mode(data$p_rate5star)
describe(data$p_rate5star)
rate1star = sum(data$p_rate1star)
rate2star = sum(data$p_rate2star)
rate3star = sum(data$p_rate3star)
rate4star = sum(data$p_rate4star)
rate5star = sum(data$p_rate5star)
rate_name = c("rate1star","rate2star","rate3star","rate4star","rate5star")
rate_number = c(rate1star,rate2star,rate3star,rate4star,rate5star)
fig <- plot_ly(type='pie', labels=rate_name, values=rate_number, 
               textinfo='label+percent',
               insidetextorientation='radial',
               )
fig <- fig %>% layout(title = "Ph???n tram dánh giá t??? 1->5 sao",uniformtext=list(minsize=8, mode='hide'))
fig
#----------------------------------------------------------------
# Dánh giá trung bình cho m???i s???n ph???m (T??? 0% -> 100%)
mode(data$p_rating)
describe(data$p_rating)
hist(data$p_rating,col = 'red',breaks=100,xlab = "Dánh giá trung bình c???a s???n ph???m (%)", ylab = "S??? lu???ng dánh giá", main = "Bi???u d??? th??? hi???n t???ng quan dánh giá s???n ph???m trên Lazada")
#----------------------------------------------------------------
# Tên shop bán hàng
mode(data$s_name)
describe(data$s_name)
#----------------------------------------------------------------
# Dánh giá trung bình cho shop (T??? 0% -> 100%)
mode(data$s_rating)
describe(data$s_rating)
hist(data$s_rating,col = 'green',breaks=10,xlab = "Dánh giá trung bình c???a c???a hàng (%)", ylab = "S??? lu???ng dánh giá", main = "Bi???u d??? th??? hi???n t???ng quan dánh giá c???a hàng trên Lazada")
#----------------------------------------------------------------
# Dánh giá trung bình ph???n h???i c???a shop cho khách hàng (T??? 0% -> 100%)
mode(data$s_response_rate)
describe(data$s_response_rate)
s_response_rate <- as.numeric(data$s_response_rate)
hist(s_response_rate,col = 'brown',breaks=15,xlab = "Dánh giá trung bình t??? l??? ph???n h???i c???a c???a hàng (%)", ylab = "S??? lu???ng dánh giá", main = "Bi???u d??? th??? hi???n t???ng quan dánh giá t??? l??? ph???n h???i c???a hàng")
#---------------------------------------------------------------
# Dánh giá trung bình th???i gian giao hàng c???a shop (T??? 0% -> 100%)
mode(data$s_ship_ontime)
describe(data$s_ship_ontime)
s_ship_ontime <- as.numeric(data$s_ship_ontime)
hist(s_ship_ontime,col = 'gray',breaks=15,xlab = "Dánh giá trung bình t??? l??? ph???n h???i c???a c???a hàng (%)", ylab = "S??? lu???ng dánh giá", main = "Bi???u d??? th??? hi???n t???ng quan dánh giá t??? l??? ph???n h???i c???a hàng")
#----------------------------------------------------------------
# M???i quan h??? c???a dánh giá trung bình s???n ph???m và dánh giá trung bình c???a hàng
ggplot(data,aes(x=s_rating,y=p_rating)) + geom_point() + geom_smooth(se=TRUE) +
  labs(title='M???i quan h??? c???a dánh giá trung bình s???n ph???m và dánh giá trung bình c???a hàng',x='Dánh giá trung bình c???a hàng (%)',y='Dánh giá trung bình s???n ph???m (%)')
#----------------------------------------------------------------
# M???i quan h??? gi???a giá ti???n và s??? lu???ng mua hàng
fig <- plot_ly(x = data$p_number_reviews, y = data$p_price,
               marker = list(size = 10,
                             color = 'rgba(255, 182, 193, .9)',
                             line = list(color = 'rgba(152, 0, 0, .8)',
                                         width = 2)))
fig <- fig %>% layout(title = 'M???i quan h??? gi???a giá ti???n và s??? lu???ng mua hàng',
                      yaxis = list(zeroline = FALSE),
                      xaxis = list(zeroline = FALSE))
fig
#----------------------------------------------------------------
# ???nh hu???ng c???a vi???c ph???n h???i khách hàng và th???i gian giao hàng d???n vi???c dánh giá s???n ph???m c???a khách hàng
fig <- plot_ly(x=data$s_ship_ontime, y=data$s_response_rate, z=data$s_rating, type = "contour",
               colorscale = 'Jet',
               autocontour = F
               )%>% layout(title = '???nh hu???ng c???a vi???c ph???n h???i khách hàng và th???i gian giao hàng d???n vi???c dánh giá s???n ph???m c???a khách hàng',
                      yaxis = list(zeroline = FALSE),
                      xaxis = list(zeroline = FALSE))
fig
#----------------------------------------------------------------
# M???i quan h??? c???a s???n ph???m chính hàng và không chính hãng d???n ch???t lu???ng s???n ph???m
fig <- plot_ly(labels = data$p_mall, values = data$p_rate1star, type = 'pie')
fig <- fig %>% layout(title = 'United States Personal Expenditures by Categories in 1960',
                      xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
                      yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))
fig
#----------------------------------------------------------------
# ???nh hu???ng s???n ph???m chính hãng và không chính hãng d???n ch???t lu???ng s???n ph???m
fig <- plot_ly(labels = data$p_mall, values = data$p_rate1star, type = 'pie',
               textposition = 'inside',
               textinfo = 'label+percent',
               insidetextfont = list(color = '#FFFFFF'),
               hoverinfo = 'text',
               marker = list(colors = colors,
                             line = list(color = '#FFFFFF', width = 1)),
               showlegend = FALSE)%>% layout(title = 'Ph???n tram dánh giá 1 sao cho kho???ng 2000 s???n ph???m chính hãng và không chính hãng',
                      xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
                      yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))
fig
fig <- plot_ly(labels = data$p_mall, values = data$p_rate5star, type = 'pie',
               textposition = 'inside',
               textinfo = 'label+percent',
               insidetextfont = list(color = '#FFFFFF'),
               hoverinfo = 'text',
               marker = list(colors = colors,
                             line = list(color = '#FFFFFF', width = 1)),
               showlegend = FALSE)%>% layout(title = 'Ph???n tram dánh giá 5 sao cho kho???ng 2000 s???n ph???m chính hãng và không chính hãng',
                                             xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
                                             yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))
fig
#----------------------------------------------------------------
# Danh m???c s???n ph???m du???c nhi???u ngu???i quan tâm
fig <- plot_ly(labels = data$p_cate, values = data$p_number_reviews, type = 'pie',
               textposition = 'inside',
               textinfo = 'label+percent',
               insidetextfont = list(color = '#FFFFFF'),
               hoverinfo = 'text',
               marker = list(colors = colors,
                             line = list(color = '#FFFFFF', width = 1)),
               showlegend = FALSE)%>% layout(title = 'Danh m???c s???n ph???m dã bán du???c',
                                             xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
                                             yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))
fig





