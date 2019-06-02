from urllib.request import urlopen
from web_parser import WebParser
from file_handler import create_project_directory, create_overview_files, create_content_file, set_to_file, list_to_file, file_to_set
import sys

class Scraper:

    def __init__(self, project_name, base_url, domain_name):
        self.project_name = project_name
        self.base_url = base_url
        self.domain_name = domain_name
        self.queue_file = project_name + "/queue.txt"
        self.scraped_file = project_name + "/scraped.txt"
        self.data_file = project_name + "/content.md"
        self.data_list = []
        self.queue = set()
        self.scraped = set()
        self.start_up()
        self.scrape_page(self.base_url, self.data_file)

    def start_up(self):
        create_project_directory(self.project_name)
        create_overview_files(self.project_name, self.base_url)
        self.queue = file_to_set(self.queue_file)
        self.scraped = file_to_set(self.scraped_file)
        print("-- Scraper initialised --")

    def scrape_page(self, page_url, data_file):
        if page_url not in self.scraped:
            create_content_file(data_file)
            self.add_links_to_queue(self.collect_links_and_data(page_url))
            self.queue.remove(page_url)
            print("Scraping: " + page_url)
            print("Queue: " + str(len(self.queue)) + " | Scraped: " + str(len(self.scraped)))
            self.scraped.add(page_url)
            self.update_files(data_file)

    def collect_links_and_data(self, page_url):
        html_string = ""
        
        try:
            response = urlopen(page_url)
            if "text/html" in response.getheader("Content-Type"):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            
            parser = WebParser(self.base_url, page_url)
            parser.feed(html_string)
            self.data_list = parser.get_data_with_tags() 
        except Exception as e:
            print("Error: " + str(e))
            print("Program terminated!")
            sys.exit()
            
        return parser.get_page_links()
    
    def add_links_to_queue(self, links):
        for url in links:
            if url in self.queue:
                continue
            if url in self.scraped:
                continue
            if self.domain_name not in url:
                continue
            self.queue.add(url)

    def update_files(self, data_file):
        set_to_file(self.queue, self.queue_file)
        set_to_file(self.scraped, self.scraped_file)
        list_to_file(self.data_list, data_file)