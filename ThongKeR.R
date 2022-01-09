#----------------------------------------------------------------
# Them thu vien
library(plotly)
library(ggplot2)
#----------------------------------------------------------------
data = read.csv("https://raw.githubusercontent.com/tranlybuu/Data_Lazada/master/LazData.csv", encoding = "UTF-8", header = TRUE)
View(data)
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
# Mô tả dữ liệu
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
# Thương hiệu
mode(data$p_brand)
describe(data$p_brand)
qplot(data$p_brand,xlab = "Thương hiệu", ylab = "Số lượng", main = "Biểu đồ số lượng sản phẩm của mỗi thương hiệu")
#---------------------------------------------------------------
# Danh mục sản phẩm
mode(data$p_cate)
describe(data$p_cate)
qplot(data$p_cate, xlab = 'Danh mục', ylab = 'Số lượng sản phẩm', main = 'Biểu đồ danh mục sản phẩm')
#----------------------------------------------------------------
# Sản phẩm chính hãng hoặc không chính hãng
mode(data$p_mall)
describe(data$p_mall)
qplot(data$p_mall, xlab = 'Sản phẩm chính hãng và không chính hãng', ylab = 'Số lượng', main = 'Biểu đồ số lượng LazMall và NonMall')
#----------------------------------------------------------------
# Tổng số lượt đánh giá cho mỗi sản phẩm
mode(data$p_number_reviews)
describe(data$p_number_reviews)
hist(data$p_number_reviews,col = 'green',breaks=40,xlab = "Số đánh giá cho mỗi sản phẩm", ylab = "Số lượng", main = "Biểu đồ thể hiện số đánh giá cho mỗi sản phẩm")
#----------------------------------------------------------------
# Giá của sản phẩm
mode(data$p_price)
describe(data$p_price)
hist(data$p_price,col = 'pink',breaks=50,xlab = "Khoảng giá sản phẩm", ylab = "Số lượng sản phẩm", main = "Biểu đồ thể hiện các khoảng giá sản phẩm")
#----------------------------------------------------------------
# Tổng số lượt đánh giá 1->5 sao cho mỗi sản phẩm
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
               insidetextorientation='radial')
fig <- fig %>% layout(title = "Phần trăm đánh giá từ 1->5 sao",uniformtext=list(minsize=8, mode='hide'))
fig
#----------------------------------------------------------------
# Đánh giá trung bình cho mỗi sản phẩm (Từ 0% -> 100%)
mode(data$p_rating)
describe(data$p_rating)
hist(data$p_rating,col = 'red',breaks=70,xlab = "Đánh giá trung bình của sản phẩm (%)", ylab = "Số lượng đánh giá", main = "Biểu đồ thể hiện tổng quan đánh giá sản phẩm trên Lazada")
#----------------------------------------------------------------
# Tên shop bán hàng
mode(data$s_name)
describe(data$s_name)
#----------------------------------------------------------------
# Đánh giá trung bình cho shop (Từ 0% -> 100%)
mode(data$s_rating)
describe(data$s_rating)
hist(data$s_rating,col = 'green',breaks=10,xlab = "Đánh giá trung bình của cửa hàng (%)", ylab = "Số lượng đánh giá", main = "Biểu đồ thể hiện tổng quan đánh giá cửa hàng trên Lazada")
#----------------------------------------------------------------
# Đánh giá trung bình phản hồi của shop cho khách hàng (Từ 0% -> 100%)
mode(data$s_response_rate)
describe(data$s_response_rate)
s_response_rate <- as.numeric(data$s_response_rate)
hist(s_response_rate,col = 'brown',breaks=15,xlab = "Đánh giá trung bình tỉ lệ phản hồi của cửa hàng (%)", ylab = "Số lượng đánh giá", main = "Biểu đồ thể hiện tổng quan đánh giá tỉ lệ phản hồi cửa hàng")
#---------------------------------------------------------------
# Đánh giá trung bình thời gian giao hàng của shop (Từ 0% -> 100%)
mode(data$s_ship_ontime)
describe(data$s_ship_ontime)
s_ship_ontime <- as.numeric(data$s_ship_ontime)
hist(s_ship_ontime,col = 'gray',breaks=15,xlab = "Đánh giá trung bình tỉ lệ phản hồi của cửa hàng (%)", ylab = "Số lượng đánh giá", main = "Biểu đồ thể hiện tổng quan đánh giá tỉ lệ phản hồi cửa hàng")
#----------------------------------------------------------------
# Mối quan hệ của đánh giá trung bình sản phẩm và đánh giá trung bình cửa hàng
ggplot(data,aes(x=s_rating,y=p_rating)) + geom_point() + geom_smooth(se=TRUE) +
  labs(title='Mối quan hệ của đánh giá trung bình sản phẩm và đánh giá trung bình cửa hàng',x='Đánh giá trung bình cửa hàng (%)',y='Đánh giá trung bình sản phẩm (%)')
#----------------------------------------------------------------
# Mối quan hệ giữa giá tiền và số lượng mua hàng
fig <- plot_ly(x = data$p_number_reviews, y = data$p_price,
               marker = list(size = 10,
                             color = 'rgba(255, 182, 193, .9)',
                             line = list(color = 'rgba(152, 0, 0, .8)',
                                         width = 2)))
fig <- fig %>% layout(title = 'Mối quan hệ giữa giá tiền và số lượng mua hàng',
                      yaxis = list(zeroline = FALSE),
                      xaxis = list(zeroline = FALSE))
fig
#----------------------------------------------------------------
# Ảnh hưởng của việc phản hồi khách hàng và thời gian gian hàng đến đánh giá sản phẩm của khách hàng
fig <- plot_ly(x=data$s_ship_ontime, y=data$s_response_rate, z=data$s_rating, type = "contour",
               colorscale = 'Jet',
               autocontour = F
)%>% layout(title = 'Ảnh hưởng của việc phản hồi khách hàng và thời gian gian hàng đến đánh giá sản phẩm của khách hàng',
            yaxis = list(zeroline = FALSE),
            xaxis = list(zeroline = FALSE))
fig
#----------------------------------------------------------------
# Ảnh hưởng của sản phẩm chính hãng và không chính hãng đến chất lượng sản phẩm
fig <- plot_ly(labels = data$p_mall, values = data$p_rate1star, type = 'pie',
               textposition = 'inside',
               textinfo = 'label+percent',
               insidetextfont = list(color = '#FFFFFF'),
               hoverinfo = 'text',
               marker = list(colors = colors,
                             line = list(color = '#FFFFFF', width = 1)),
               showlegend = FALSE)%>% layout(title = 'Phần trăm đánh giá 1 sao cho khoảng 2000 sản phẩm chính hãng và không chính hãng',
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
               showlegend = FALSE)%>% layout(title = 'Phần trăm đánh giá 5 sao cho khoảng 2000 sản phẩm chính hãng và không chính hãng',
                                             xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
                                             yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))
fig
#----------------------------------------------------------------
# Phẩn trăm sản phẩm khách hàng quan tâm
fig <- plot_ly(labels = data$p_cate, values = data$p_number_reviews, type = 'pie',
               textposition = 'inside',
               textinfo = 'label+percent',
               insidetextfont = list(color = '#FFFFFF'),
               hoverinfo = 'text',
               marker = list(colors = colors,
                             line = list(color = '#FFFFFF', width = 1)),
               showlegend = FALSE)%>% layout(title = 'Phần trăm danh mục sản phẩm được khách hàng tiêu thụ',
                                             xaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE),
                                             yaxis = list(showgrid = FALSE, zeroline = FALSE, showticklabels = FALSE))
fig

