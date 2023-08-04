import scrapy

class RentProp(scrapy.Spider):
    name = "property-pro"

    # This gets the data for everything on the website
    start_urls = [f"https://www.propertypro.ng/{prop_type}search=&auto=&type=&bedroom=&min_price=&max_price=&page={page_numb}" for prop_type in ["property-for-sale?", "property-for-rent?", "property-for-short-let?", "properties/land?"] for page_numb in range(843)]


    def start_request(self):
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
            


    def parse(self, response):
        # This will loop through each page
        for prop in response.css('div.single-room-text'):
            url_resp = response.url
            prop_type = "Not Defined"
            if "rent" in url_resp:
                prop_type = "Property for rent"
            elif "short-let" in url_resp:
                prop_type = "Property for shortlet"
            elif "land" in url_resp:
                prop_type = "Land"

            title = prop.css('div.single-room-text > a > h4::text').get()
            location = prop.css('div.single-room-text > h4::text').get()

            # Currency and Price 
            currency = prop.css('div.n50 > h3 > span:nth-child(1)::text').get()
            price = prop.css('div.n50.featured-text > h3 > span:nth-child(2)::text').getall()

            # Bedrooms, baths and toilets
            bedrooms = prop.css('div.single-room-text > div.fur-areea > span:nth-child(1)::text').get()
            baths = prop.css('div.single-room-text > div.fur-areea > span:nth-child(2)::text').get()
            toilets = prop.css('div.single-room-text > div.fur-areea > span:nth-child(3)::text').get()

            date_added = prop.css('div.single-room-text > h5::text').getall()
            phone_number = prop.css('div.phone-icon::text').getall()

            # Cleaning it up a bit
            currency, price, phone_number, date_added = "".join(currency),"".join(price), "".join(phone_number).strip('\n'), "".join(date_added).strip('\n') 

            # This will follow the read more and extract the data stored there
            read_more_url = prop.css("div.result-list-details > p > a::attr('href')").get()
            more_det_url = response.urljoin(read_more_url)

            # This gets the details for the page
            content = {"Property Type": prop_type, "Title": title, "Location": location, "Bedrooms": bedrooms, "Baths": baths, "Toilets": toilets, 
            "Price": f"{currency}{price}", "Date Added": date_added, "Contact": phone_number}

            # Gets to the more details page
            more_details = scrapy.Request(more_det_url, callback=self.get_details, cb_kwargs={"content": content})
            yield more_details
            

    def get_details(self, response, content):
        # This function will get the details from each read more
        more_details = response.css("#tabs-1 > div > div.key-features-area > div.description-area")

        for det in more_details:
            details = det.css("*::text").getall()
            # This cleans up the more details page
            details = "".join(details).strip()

            content["More Details"] = details # Assigns the more details page per read more to each content
            yield content
