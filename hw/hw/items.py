# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MovieItem(scrapy.Item):
    Rank = scrapy.Field()
    Title = scrapy.Field()
    Year = scrapy.Field()
    Directed_by = scrapy.Field()
    Box_office = scrapy.Field()
    movie_url = scrapy.Field()