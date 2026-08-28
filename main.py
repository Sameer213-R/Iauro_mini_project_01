from scraper.fetcher import WebFetcher
from scraper.parser import HTMLParser
from scraper.extractor import DataExtractor
from scraper.exporter import JSONExporter
import os

url = os.getenv("URL")

fetcher = WebFetcher()
parser = HTMLParser()
extractor = DataExtractor()
exporter = JSONExporter()


html = fetcher.fetch(url)

soup = parser.parse(html)

data = extractor.extract(soup)

data["url"] = url

exporter.save(
    data,
    "output/data.json"
)