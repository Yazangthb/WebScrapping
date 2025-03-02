# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class MoviePipeline:
    def process_item(self, item, spider):
        # Add any processing logic here (e.g., cleaning data, validating fields)
        item["Rank"] = item.get("Rank", "N/A").strip()
        item["Title"] = item.get("Title", "").strip()
        item["Year"] = item.get("Year", "N/A").strip()
        item["Directed_by"] = item.get("Directed_by", "N/A").strip()
        item["Box_office"] = item.get("Box_office", "N/A").strip()
        return item
    
    
import mysql.connector

class SaveToMysqlPipeline:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1945",
            database="movies"
        )

        self.cursor = self.db.cursor()
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        title VARCHAR(255),
        year VARCHAR(255),
        `rank` VARCHAR(255),
        directed_by VARCHAR(255),
        box_office VARCHAR(255)
    )
""")



    def process_item(self, item, spider):
        self.cursor.execute(
    "INSERT INTO movies (title, year, `rank`, directed_by, box_office) VALUES (%s, %s, %s, %s, %s)",
    (item["Title"], item["Year"], item["Rank"], item["Directed_by"], item["Box_office"])
)

        self.db.commit()
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()