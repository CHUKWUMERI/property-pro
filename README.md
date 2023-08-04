# Nigerian Housing Dataset
This is a web scraping project built using Scrapy, a powerful and flexible web scraping framework in Python. The purpose of this scraper is to collect Nigerian property information from the "propertypro.ng" and store it in a structured format.

# How it works
The scraper starts by sending requests to the website's search result pages, extracting property details such as title, location, price, number of bedrooms, baths, and toilets, date added, and contact information. For each property, it then follows the "Read More" link to extract additional details about the property.

The scraped data is saved in CSV format to a file. The CSV file contains details for each property, including the "property type" field, which stores the type of the property.

# Features
Scrapes rental property information from "propertypro.ng" website.
Retrieves data from multiple pages by following pagination links.
Extracts detailed information from individual property pages.
Stores the scraped data in a structured CSV format.
Provides flexibility to be extended for further data analysis or integration with other tools.

# Usage
Install the required libraries by running pip install scrapy.
Clone this repository using git clone https://github.com/chukwumeri/rental-property-scraper.git.
Navigate to the project directory: cd rental-property-scraper.
Execute the scraper using the command: scrapy crawl property-pro -o "file-name.csv".
The scraper will start collecting data and save it to "file-name.csv" in the project directory.

# Contributing
Contributions to this project are welcome! Whether you find bugs, have suggestions for improvements, or want to add new features, feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License.
