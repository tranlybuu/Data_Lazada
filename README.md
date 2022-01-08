<p align="center"><img src="https://user-images.githubusercontent.com/70121634/148651256-2c8d908d-6fec-487f-ac02-977e98ed89f7.png" alt="Lazada" height="200"/></p>
<h1 align="center">Product data on Lazada</h1>
<h3 align="center">Kaggle: https://www.kaggle.com/tranlybuu/lazada-product-data</h3>

Thư mục **LAZADA** => Crawl dữ liệu các sản phẩm thuộc tất cả danh mục và thống kê

LAZADA/**url.txt** chứa tất cả đường dẫn url danh mục các sản phẩm

LAZADA/**history.txt** chứa tất cả đường dẫn url các sản phẩm đã lấy dữ liệu

LAZADA/**output.csv** các file output là file chứa tất cả các dữ liệu về sản phẩm **chưa qua xử lý**

**LazadaProductData.json** chứa tất cả các dữ liệu về sản phẩm **chưa qua xử lý** ở dạng JSON

**LazData.csv** chứa tất cả các dữ liệu về sản phẩm **đã qua xử lý** ở dạng CSV

**update_data.py** đọc dữ liệu các file **output** sau đó xử lý dữ liệu và thêm dữ liệu vào **LazData.csv**

**ThongKePython.ipynb** thống kê dữ liệu được lấy từ **LazData.csv** bằng Python

**ThongKeR.ipynb** thống kê dữ liệu được lấy từ **LazData.csv** bằng R

**Để crawl dữ liệu**: Để đường dẫn danh mục sản phẩm bạn muốn crawl vào **LAZADA/url.txt** >> Mở terminal tại **DataLaza/LAZADA** >> **scrapy crawl lazada_bot -o <tên_file_csv>.csv**

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
