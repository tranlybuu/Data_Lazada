Thư mục **LAZADA** => Crawl dữ liệu các sản phẩm thuộc tất cả danh mục và thống kê

LAZADA/**url.txt** chứa tất cả đường dẫn url danh mục các sản phẩm

LAZADA/**output.csv** các file output là file chứa tất cả các dữ liệu về sản phẩm **chưa qua xử lý**

LAZADA/**history.txt** chứa tất cả đường dẫn url các sản phẩm đã lấy dữ liệu

**LazData.csv** chứa tất cả các dữ liệu về sản phẩm **đã qua xử lý**

**thongke.ipynb** thống kê dữ liệu được lấy từ **LazData.csv**

**update_data.py** đọc dữ liệu các file **output** sau đó xử lý dữ liệu và thêm dữ liệu vào **LazData.csv**

Để crawl dữ liệu: Mở terminal tại **DataLaza/LAZADA** >> scrapy crawl lazada_bot -o <tên_file_csv>.csv

Hiện tại crawl được **17** thông tin của sản phẩm:

- **p_name**              - Tên sản phẩm

- **p_brand**             - Tên thương hiệu sản phẩm

- **p_cate**              - Danh mục sản phẩm

- **p_price**             - Giá sản phẩm

- **p_rating**            - Đánh giá trung bình của sản phẩm

- **p_image**             - Đường dẫn ảnh sản phẩm

- **p_mall**              - Chứng nhận Lazada Mall

- **p_number_reviews**    - Tổng số lượt đánh giá sản phẩm

- **p_rate1star**         - Tổng số đánh giá 1 sao cho sản phẩm

- **p_rate2star**         - Tổng số đánh giá 2 sao cho sản phẩm

- **p_rate3star**         - Tổng số đánh giá 3 sao cho sản phẩm

- **p_rate4star**         - Tổng số đánh giá 4 sao cho sản phẩm

- **p_rate5star**         - Tổng số đánh giá 5 sao cho sản phẩm

- **s_name**              - Tên nhà bán hàng

- **s_rating**            - Tỉ lệ đánh giá cho nhà bán hàng

- **s_response_rate**     - Tỉ lệ nhà bán hàng phản hồi

- **s_ship_ontime**       - Tỉ lệ nhà bán hàng giao hàng đúng giờ
