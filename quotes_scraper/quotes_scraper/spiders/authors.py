import scrapy

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    custom_settings = {
        'FEEDS': {
            'quotes_scraper/authors.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'indent': 4,
            },
        },
    }

    def parse(self, response):
        author_links = response.xpath('//div[@class="quote"]/span/a/@href').getall()
        for link in author_links:
            yield response.follow(link, self.parse_author)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        yield {
            'fullname': response.xpath('//h3[@class="author-title"]/text()').get().strip(),
            'born_date': response.xpath('//span[@class="author-born-date"]/text()').get(),
            'born_location': response.xpath('//span[@class="author-born-location"]/text()').get().strip(),
            'description': ' '.join(response.xpath('//div[@class="author-description"]/text()').getall()).strip()
        }
