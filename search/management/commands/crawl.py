import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from search_app.models import WebPage

class Command(BaseCommand):
    help = 'Crawl websites and store content'

    def handle(self, *args, **options):
        # Implement your crawling logic here
        # This is a very basic example
        urls = ['https://example.com', 'https://example.org']
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No title'
            content = soup.get_text()
            WebPage.objects.update_or_create(
                url=url,
                defaults={'title': title, 'content': content}
            )
        self.stdout.write(self.style.SUCCESS('Crawling completed'))