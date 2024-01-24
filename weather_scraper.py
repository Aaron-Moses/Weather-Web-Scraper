from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

BASE_URL = 'https://www.theweathernetwork.com/ca/weather/ontario'
CITIES = ['london', 'toronto', 'vaughan']
LOAD_WAIT_TIME = 10

def extract_temperature(temp_str):
    match = re.search(r'-?\d+', temp_str)
    return match.group(0) if match else None

def add_units(label, value):
    units = {
        'Wind': 'km/h', 'Humidity': '%', 'Visibility': 'km',
        'Pressure': 'kPa', 'Ceiling': 'm', 'Sunrise': 'am',
        'Sunset': 'pm', 'Wind gust': 'km/h',
    }
    return f"{value}{units.get(label, '')}"

def get_weather_data(city):
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        url = f'{BASE_URL}/{city}'
        driver.get(url)
        WebDriverWait(driver, LOAD_WAIT_TIME).until(EC.presence_of_element_located((By.CLASS_NAME, 'temp')))

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup

def print_weather_data(soup, city):
    temperature_element = soup.find('span', class_='temp')
    feels_like_element = soup.find('p', class_='feels-like')
    if temperature_element and feels_like_element:
        temperature = extract_temperature(temperature_element.get_text(strip=True))
        feels_like_temp = extract_temperature(feels_like_element.find('span', class_='value').get_text(strip=True))
        print(f"Weather in {city.title().replace('-', ' ')}:")
        print(f"  Temperature: {temperature} C")
        print(f"  Feels Like: {feels_like_temp} C")
    else:
        print(f"Weather data not found for {city.title().replace('-', ' ')}.")

    for div in soup.find_all('div', class_='detailed-metrics'):
        label_span = div.find('span', class_='label')
        value_span = div.find('span', class_='value')
        if label_span and value_span:
            label = label_span.get_text(strip=True)
            value = value_span.get_text(strip=True)
            print(f"  {label}: {add_units(label, value)}")
        else:
            print("  Metric data not found in this div.")
    print("\n")

def main():
    for city in CITIES:
        soup = get_weather_data(city)
        print_weather_data(soup, city)

if __name__ == "__main__":
    main()
