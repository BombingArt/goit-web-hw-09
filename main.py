from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_scraper.quotes_scraper.spiders.quotes import QuotesSpider
from quotes_scraper.quotes_scraper.spiders.authors import AuthorsSpider
from data.format_data import format_and_delete_files
from database.seed import seed_database

# об'єднав до купи скрапінг, форматування отриманих json, видалення непотрібних json і завантаження даних до бд

# код бд з минулого завдання довелось трохи модифікувати, але зміни незначні, здебільшого в імпортах та шляхах до файлів

# усі отримані відформатовані json лежать в директорії data/json

def main():
    process = CrawlerProcess(get_project_settings())

    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)
    process.start()

    format_and_delete_files('quotes_scraper/quotes.json', 'quotes_scraper/authors.json')

    seed_database()

    print("Data scraped, formatted, and loaded into the database successfully.")

    

if __name__ == "__main__":
    main()
