# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    Hotel_Name = scrapy.Field()
    Numberof_Ratings = scrapy.Field()
    Hotel_Type = scrapy.Field()