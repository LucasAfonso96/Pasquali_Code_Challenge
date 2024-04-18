import sys
import concurrent.futures
from extractor import extract_logo, extract_phone_numbers
from utils import format_output

def process_website(url):
    logo_url = extract_logo(url)
    phone_numbers = extract_phone_numbers(url)

    return format_output(logo_url, phone_numbers, url)

def main():
    urls = [line.strip() for line in sys.stdin if line.strip()]  
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_website, urls))
    for result in results:
        print(result)

if __name__ == "__main__":
    main() 