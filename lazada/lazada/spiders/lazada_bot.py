import re
import os
import scrapy
from ..items import LazadaItem
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from scrapy.utils.project import get_project_settings

class LazadaBotSpider(scrapy.Spider):
    name = 'lazada_bot'

    def start_requests(self):

        path = "E:\dataLazada\lazada"       # Đường dẫn đến thư mục chứa url.txt
        os.chdir(path)

        file = open('url.txt', 'r', encoding='UTF-8')  #====================+
        data_url_cate = file.readlines()               #  Đọc file url.txt  | 
        file.close()                                   #====================+

        # data_url_cate = ['https://www.lazada.vn/laptop/',]

        number_of_pages = 2         # Số lượng trang sẽ cào ở mỗi danh mục sản phẩm
        
        url_cate_list = []
        for item in data_url_cate:
            for count_page in range(1,number_of_pages):
                url = str(item) + "?page=" + str(count_page)
                url_cate_list.append(url)

        

        for item in url_cate_list:
            settings= get_project_settings()
            driver_path = 'E:\dataLazada\lazada\chromedriver.exe'
            options= webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome(driver_path, options=options)
            driver.get(item)
            link_elements = driver.find_elements_by_xpath('//*[@data-qa-locator="product-item"]//a[text()]')
            for link in link_elements:
                # yield scrapy.Request(link.get_attribute('href'), callback=self.parse)
                link = link.get_attribute('href')
                yield SeleniumRequest(
                    url = link,
                    wait_time = 3,
                    screenshot = True,
                    callback = self.parse,
                    dont_filter = True
                )
            driver.quit()


    def parse(self, response):
        p_image = response.css('.gallery-preview-panel__image').css("::attr(src)").extract()
        #<h1 class="pdp-mod-product-badge-title" data-spm-anchor-id="a2o4n.pdp_revamp.0.i0.7001594b3uSzoB">COOLMATE Áo thun nam Cotton Compact ngắn tay phiên bản Premium chống nhăn, thoáng mát nhiều màu</h1>
        p_name = response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get()
        #<span class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl" data-spm-anchor-id="a2o4j.pdp_revamp.0.i4.5374460fXeWzZg">Rp108.500</span>
        p_price = response.xpath('//span[@class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()').get()
        #<span class="score-average" data-spm-anchor-id="a2o4n.pdp_revamp.ratings_reviews.i1.63e45ac3btUWq5">4.9</span>
        p_rating = response.xpath('//div[@class="score"]/span[@class="score-average"]/text()').get()
        #<a class="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name" target="_self">Teeworld Fashion - Thế Giới Áo Thun</a>
        s_name = response.xpath('//a[@class="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name"]/text()').get()
        #<div class="seller-info-value rating-positive ">92%</div>
        s_rating = response.xpath('//div[@class="seller-info-value rating-positive "]/text()').get()
        #<a title="Quần áo nam" class="breadcrumb_item_anchor" data-spm-anchor-id="a2o4n.pdp_revamp.breadcrumb.2">
        p_cate = response.xpath('//a[@class="breadcrumb_item_anchor"]/span[1]/text()').get()
        #<div class="pdp-mod-product-badge-wrapper"><img src="https://laz-img-cdn.alicdn.com/imgextra/i1/O1CN01JUOYif22N3Uu7JX4R_!!6000000007107-2-tps-162-48.png"
        p_mall = response.xpath('//div[@class="pdp-mod-product-badge-wrapper"]/img[1]').get()
        #<a class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-review-summary__link" data-spm-anchor-id="a2o4n.pdp_revamp.0.0">4 đánh giá</a>
        p_number_reviews = response.xpath('//a[@class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-review-summary__link"]/text()').get()
        #<div style="color:" class="seller-info-value " data-spm-anchor-id="a2o4n.pdp_revamp.seller.i0.7a7c4ec6FpEtdG">100%</div>
        s_ship_ontime = response.xpath('//div[@class="info-content"][2]/div[2]/text()').get()
        #<div style="color:" class="seller-info-value " data-spm-anchor-id="a2o4n.pdp_revamp.seller.i1.7a7c4ec6FpEtdG">100%</div>
        s_response_rate = response.xpath('//div[@class="info-content"][3]/div[2]/text()').get()
        #<a class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link" target="_self" data-spm-anchor-id="a2o4n.pdp_revamp.0.0">HADES</a>
        p_brand = response.xpath('//a[@class="pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link"]/text()').get()

        

        p_rate5star = response.xpath('//div[@class="detail"]/ul[1]/li[1]/span[@class="percent"]/text()').get()
        p_rate4star = response.xpath('//div[@class="detail"]/ul[1]/li[2]/span[@class="percent"]/text()').get()
        p_rate3star = response.xpath('//div[@class="detail"]/ul[1]/li[3]/span[@class="percent"]/text()').get()
        p_rate2star = response.xpath('//div[@class="detail"]/ul[1]/li[4]/span[@class="percent"]/text()').get()
        p_rate1star = response.xpath('//div[@class="detail"]/ul[1]/li[5]/span[@class="percent"]/text()').get()

        # Xử lý với các mặt hàng thuộc Lazada Mall
        try:
            if len(p_mall)>0:
                p_mall = "Mall"
        except:
            p_mall = "Non-Mall"

        item = LazadaItem()
        item["p_name"] = p_name
        item["p_cate"] = p_cate
        item['p_price'] = p_price
        item["p_rating"] = p_rating
        item["p_brand"] = p_brand
        item["s_name"] = s_name
        item["s_rating"] = s_rating
        item["p_mall"] = p_mall
        item["p_image"] = p_image
        item["p_number_reviews"] = p_number_reviews
        item["s_ship_ontime"] = s_ship_ontime
        item["s_response_rate"] = s_response_rate
        item["p_rate5star"] = p_rate5star
        item["p_rate4star"] = p_rate4star
        item["p_rate3star"] = p_rate3star
        item["p_rate2star"] = p_rate2star
        item["p_rate1star"] = p_rate1star
        yield item