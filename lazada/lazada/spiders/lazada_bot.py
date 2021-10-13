import scrapy
from ..items import LazadaItem

class LazadaBotSpider(scrapy.Spider):
    name = 'lazada_bot'
    allowed_domains = ['lazada.vn']
    start_urls = [
        'https://www.lazada.vn/products/dirtycoins-graffitee-t-shirt-i933984590-s2806198075.html?spm=a2o4n.searchlist.list.1.38001c0dpor8Pn&search=1',
        'https://www.lazada.vn/products/hcmvoucher-10-ao-thun-teeworld-saigonese-the-city-that-never-sleeps-t-shirt-i930026101-s2784942937.html?spm=a2o4n.pdp_revamp.recommend_2.2.63e45ac3btUWq5&mp=1&cid=0&mp=1&impsrc=&ad_src=1400_522:0.035714,1400_900:0.964308150458767,1400_910:0.999097447997711&cpc=52529&originalCpc=72700&pos=1&highest_price=72700&pa=sponsored_bottom&did=8a455e05-21ab-491e-abad-a6ee128a902b&abid=0,195686,237633,8460342,10909572,10909594,12091908,12189920,12192856,12346160,12442230,12449264,12457386,12523892,12524908,12559244,12575250,12587260,12618398,12656138,12700250,12732130&adFlag=3&adid=0&bucketId=0&sellerId=1000342339&itemId=930026101&member_id=158001307&ncid=101100009622057&adgroup_id=424354331&creative_id=929304134&brand_id=65074&category_id=7930&regional_key=090205020100&pdp_item=933984590&pid_pvid=e43211f4d41d464a53760ccf657265d7&nick=&pvid=8a455e05-21ab-491e-abad-a6ee128a902b&pvtime=1634039876&ad_src=1400_522:0.035714,1400_900:0.964308150458767,1400_910:0.999097447997711&crowd_id=&one_id=',
        'https://www.lazada.vn/products/dien-thoai-iphone-x-64g-256g-quoc-te-moi-98-i1350654989-s5565368781.html?spm=a2o4n.home.just4u.20.4935e182l9M3Uc&scm=1007.17519.162103.0&pvid=756a5a68-d3f5-46fd-8fbe-9f930863345d&search=0&clickTrackInfo=tctags%3A1216475156+1285875519%3Btcsceneid%3AHPJFY%3Bbuyernid%3A7ad5fd1a-d9f1-43de-e917-fa99f2b65de9%3Btcboost%3A0%3Bpvid%3A756a5a68-d3f5-46fd-8fbe-9f930863345d%3Bchannel_id%3A0000%3Bmt%3Ai2i%3Bitem_id%3A1350654989%3Bself_ab_id%3A162103%3Bself_app_id%3A7519%3Blayer_buckets%3A5437.25236_6059.28891_955.3630%3Bpos%3A20%3B',
        'https://www.lazada.vn/products/hop-qua-bi-an-i1254836052-s4681427315.html?spm=a2o4n.home.just4u.10.158de182mZI11y&scm=1007.17519.162103.0&pvid=62bc98f8-76e3-404e-9fce-1713c6dbfea4&search=0&clickTrackInfo=tcsceneid%3AHPJFY%3Bbuyernid%3A7ad5fd1a-d9f1-43de-e917-fa99f2b65de9%3Btcboost%3A0%3Bpvid%3A62bc98f8-76e3-404e-9fce-1713c6dbfea4%3Bchannel_id%3A0000%3Bmt%3Ai2i%3Bitem_id%3A1254836052%3Bself_ab_id%3A162103%3Bself_app_id%3A7519%3Blayer_buckets%3A5437.25236_955.3631_955.3630_6059.28889%3Bpos%3A10%3B',
        'https://www.lazada.vn/products/hop-qua-bi-an-tri-an-khach-hang-tang-1-hop-qua-qua-tang-chamy-i975506473-s3066122591.html?&search=pdp_v2v?spm=a2o4n.pdp_revamp.recommendation_2.4.5e431266Opgrw6&mp=1&scm=1007.16389.126158.0&clickTrackInfo=e7a30717-0aed-4934-9c37-62c018782288__975506473__13036__trigger2i__202835__0.623__0.623__0.0__0.0__0.0__0.623__3__8__PDPV2V__251__null__1285875519%201216475156__0____20000.0__0.5325__3.6511627906976742__129__9350.0__129536,129632,105538,129730,135745,138442,129643,98762,132009,103150,113326,110577,96816,129332,138522,96856,138811,128698,129114,98588__null__null__null__3650.16544_955.3632_3650.16542__null__13499__null__0.0__0.0__elp.2_star.6_starplus.3__'
        ]

    def parse(self, response):
        #<h1 class="pdp-mod-product-badge-title" data-spm-anchor-id="a2o4n.pdp_revamp.0.i0.7001594b3uSzoB">COOLMATE Áo thun nam Cotton Compact ngắn tay phiên bản Premium chống nhăn, thoáng mát nhiều màu</h1>
        p_name = response.xpath('//h1[@class="pdp-mod-product-badge-title"]/text()').get()
        #<span class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl" data-spm-anchor-id="a2o4j.pdp_revamp.0.i4.5374460fXeWzZg">Rp108.500</span>
        p_price = response.xpath('//span[@class=" pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl"]/text()').get()
        #<span class="score-average" data-spm-anchor-id="a2o4n.pdp_revamp.ratings_reviews.i1.63e45ac3btUWq5">4.9</span>
        p_rating = response.xpath('//span[@class="score-average"]/text()').get()
        #<a class="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name" target="_self">Teeworld Fashion - Thế Giới Áo Thun</a>
        s_name = response.xpath('//a[@class="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name"]/text()').get()
        #<div class="seller-info-value rating-positive ">92%</div>
        s_rating = response.xpath('//h1[@class="seller-info-value rating-positive "]/text()').get()
        #<a title="Quần áo nam" class="breadcrumb_item_anchor" data-spm-anchor-id="a2o4n.pdp_revamp.breadcrumb.2">
        p_cate = response.xpath('//a[@class="breadcrumb_item_anchor"]/span[1]/text()').get()
        #<div class="pdp-mod-product-badge-wrapper"><img src="https://laz-img-cdn.alicdn.com/imgextra/i1/O1CN01JUOYif22N3Uu7JX4R_!!6000000007107-2-tps-162-48.png"
        p_mall = response.xpath('//div[@class="pdp-mod-product-badge-wrapper"]/img[1]').get()
        

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
        item["s_name"] = s_name
        item["s_rating"] = s_rating
        item["p_mall"] = p_mall
        yield item