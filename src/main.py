import sys
import threading
from extractor import extract_logo, extract_phone_numbers
from utils import format_output

def process_website(url):
    logo_url = extract_logo(url)
    phone_numbers = extract_phone_numbers(url)

    return format_output(logo_url, phone_numbers, url)

def process_multiple_websites(urls):
    threads = []
    results = []

    def process_url(url):
        result = process_website(url)
        results.append(result)

    for url in urls:
        thread = threading.Thread(target=process_url, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results

def main():
    urls = [line.strip() for line in sys.stdin if line.strip()]  
    results = process_multiple_websites(urls)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
