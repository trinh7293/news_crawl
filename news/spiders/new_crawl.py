import scrapy
from news.items import NewsItem
from news.database.firestore import db, add_data

class QuotesSpider(scrapy.Spider):
    name = "news"

    start_urls = [
        'https://www.24h.com.vn/aff-cup-2018-c827.html',
    ]
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        extract_urls = response.css('article.bxDoiSbIt header a::attr(href)').extract()
        for url in extract_urls:
            yield scrapy.Request(url=url, callback=self.extract_content)


    def extract_content(self, response):
        # Title
        title = response.css('header h1.clrTit::text').extract()[0].strip()
        # Summary
        summary = response.css('article h2.ctTp::text').extract()[0].strip()
        # Content
        list_paragraph = response.css('article p::text').extract()
        l = [pa.strip() for pa in list_paragraph]
        content = '\n'.join(l)

        # Save
        # item = NewsItem()
        # item['title'] = title
        # item['summary'] = summary
        # item['content'] = content
        add_data({
            'title': title,    
            'summary': summary,    
            'content': content        
        }, '24h_news')
        # yield item
          
