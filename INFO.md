Thư mục **LAZADA** => Crawl dữ liệu các sản phẩm thuộc tất cả danh mục và thống kê

Thư mục **CATEGORY** => Crawl tất cả các đường dẫn url danh mục sản phẩm

LAZADA/**output.csv** chứa tất cả các dữ liệu về sản phẩm nhưng chưa qua xử lý

LAZADA/**thongke.ipynb** xử lý dữ liệu và thống kê

LAZADA/**url.txt** chứa tất cả đường dẫn url danh mục các sản phẩm thu được từ quá trình crawl **CATEGORY**

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
