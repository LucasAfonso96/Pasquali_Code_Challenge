import requests
from bs4 import BeautifulSoup
import re
import sys
from utils import clean_phone_number

def extract_logo(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            logo_image = soup.find('img', class_=re.compile('.*logo.*'))
            if logo_image:
                logo_src = logo_image['src']
                return logo_src
            else:
                print("No logo image found", file=sys.stderr)
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}", file=sys.stderr)
    except Exception as e:
        print(f"Error extracting logo from {url}: {e}", file=sys.stderr)
    return None

def extract_phone_numbers(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        phone_numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', response.text)
        cleaned_numbers = [clean_phone_number(number) for number in phone_numbers]
        return cleaned_numbers
    except Exception as e:
        print(f"Error extracting phone numbers from {url}: {e}" , file=sys.stderr)
    return []
