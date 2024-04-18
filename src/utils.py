import re
import json

def clean_phone_number(phone_number):
    cleaned_number = re.sub(r'[^\d\+\(\)]', ' ', phone_number)
    cleaned_number = re.sub(r'\s+', ' ', cleaned_number)
    return cleaned_number.strip()

def format_output(logo_url, phone_numbers, url):
    output = {
        "logo_url": logo_url,
        "phone_numbers": phone_numbers,
        "website" : url
    }
    return json.dumps(output)
