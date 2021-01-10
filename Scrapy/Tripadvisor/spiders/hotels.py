import scrapy
from ..items import TripadvisorItem

class Manipalhotels (scrapy.Spider):
    name = 'hotel'
    page_number = 30
    start_urls = [
   'https://www.tripadvisor.in/Restaurants-g737163-Manipal_Udupi_District_Karnataka.html'
   ]
    
    def parse(self, response):
        
        items = TripadvisorItem()
        
        
        
        all_div_hotels = response.css('div._1llCuDZj')
        
        for h in all_div_hotels:
            Hotel_Name = h.css('._15_ydu6b::text').extract()
            Numberof_Ratings = h.css('.w726Ki5B::text').extract_first()
            Hotel_Type = h.css('._3d9EnJpt .EHA742uW:nth-child(1) ._1p0FLy4t::text').extract_first()        
           
            items['Hotel_Name'] = Hotel_Name
            items['Numberof_Ratings'] = Numberof_Ratings
            items['Hotel_Type'] = Hotel_Type
            
            yield items
                
        next_page = 'https://www.tripadvisor.in/Restaurants-g737163-oa'+str(Manipalhotels.page_number) +'-Manipal_Udupi_District_Karnataka.html'
        if Manipalhotels.page_number <= 90:
          yield response.follow (next_page,callback=self.parse)  
          Manipalhotels.page_number += 30
          
   
     
        