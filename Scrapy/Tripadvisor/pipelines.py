# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter

import sqlite3

class TripadvisorPipeline(object):
    
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect("myhotels.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
            self.curr.execute("""DROP TABLE IF EXISTS hotels""")
            self.curr.execute(""" create table hotels (
               Hotel_Name text,
               Numberof_Ratings text,
               Hotel_Type text )
               """)
                              
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into hotels values (?,?,?)""",
                          (item['Hotel_Name'][2],
                           item['Numberof_Ratings'],
                           item['Hotel_Type']
            
                              ))
        self.conn.commit()