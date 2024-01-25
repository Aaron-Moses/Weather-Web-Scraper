# Weather Scraper README

## Overview
This script scrapes weather data from The Weather Network for Ontario cities using Selenium and BeautifulSoup.

## Prerequisites
- Python 3.x
- Selenium
- BeautifulSoup4
- WebDriver Manager for Chrome

## Installation
pip install selenium beautifulsoup4 webdriver-manager

## Usage
- Set desired cities in `CITIES` list.
- Run script:
python weather_scraper.py

## Functions
- `extract_temperature()`: Extracts temperature from string.
- `add_units()`: Adds units to weather metrics.
- `get_weather_data()`: Retrieves HTML for city weather.
- `print_weather_data()`: Prints weather data.
- `main()`: Main function to process cities.

## Limitations
- Limited to predefined cities.
- Dependent on website's HTML structure.

## License
MIT License
