import json
import os

def format_and_delete_files(quotes_file, authors_file):
    json_dir = 'data/json'
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    def format_quotes(quotes_file):
        with open(quotes_file, 'r', encoding='utf-8') as file:
            quotes_data = json.load(file)
        
        formatted_quotes = []
        for quote_data in quotes_data:
            formatted_quote = {
                'tags': quote_data['tags'],
                'author': quote_data['author'],
                'quote': quote_data['quote']
            }
            formatted_quotes.append(formatted_quote)
        
        return formatted_quotes

    def format_authors(authors_file):
        with open(authors_file, 'r', encoding='utf-8') as file:
            authors_data = json.load(file)
        
        formatted_authors = []
        for author_data in authors_data:
            formatted_author = {
                'fullname': author_data['fullname'],
                'born_date': author_data['born_date'],
                'born_location': author_data['born_location'],
                'description': author_data['description']
            }
            formatted_authors.append(formatted_author)
        
        return formatted_authors

    def delete_files(*files):
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    quotes_formatted = format_quotes(quotes_file)
    with open(os.path.join(json_dir, 'quotes.json'), 'w', encoding='utf-8') as file:
        json.dump(quotes_formatted, file, ensure_ascii=False, indent=4)

    authors_formatted = format_authors(authors_file)
    with open(os.path.join(json_dir, 'authors.json'), 'w', encoding='utf-8') as file:
        json.dump(authors_formatted, file, ensure_ascii=False, indent=4)

    delete_files(quotes_file, authors_file)
    
    return "Data formatted successfully and old files deleted."

if __name__ == "__main__":
    result_message = format_and_delete_files('quotes_scraper\\quotes.json', 'quotes_scraper\\authors.json')
    print(result_message)
