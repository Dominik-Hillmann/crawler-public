# External libraries
from bs4 import BeautifulSoup
# # Self-written
# from PageTypes import PageTypes
# from URLWrapper import URLWrapper

class URLsExtractor:
    
    def __init__(self, html):
        self.html_soup = BeautifulSoup(html, 'html.parser')


    def get_urls(self):
        return self._urls_from_search()


    ###################
    # Private methods #
    ###################

    def _urls_from_search(self):
        extracted_urls = []
        img_elements = self.html_soup.find_all('img', { 'class': 'd-block' })

        for img_element in img_elements:
            url = img_element['src'].encode('utf-8')
            extracted_urls.append(url)

        return extracted_urls
