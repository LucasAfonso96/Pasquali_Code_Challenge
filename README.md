# Pasquali Code Challange

## Technical Overview

This repository contains Python scripts for extracting logo URLs and phone numbers from webpages. The main script, `main.py`, reads URLs from standard input, processes them concurrently using multithreading, and outputs the results in JSON format.

### Features
- **Multithreading**: Utilizes threading to process multiple URLs concurrently, improving efficiency.
- **Output Formatting**: Formats extracted data (logo URL, phone numbers, and website URL) into JSON objects for easy consumption.
- **Regular Expressions (regex)**: Usage of regex for extracting phone numbers from webpage content, ensuring flexibility and accuracy in pattern matching.
- **BeautifulSoup**: Utilizes BeautifulSoup library for parsing HTML content and extracting logo URLs,
- **Observation**: I didn't use any framework like Flask or FastApi because the simplicity of the code challenge, if had more API complexity I would certainly use one of them.


### Windows

1. **Install Docker Desktop:**
   - Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) for Windows.

2. **Open PowerShell or Command Prompt:**
   - Open PowerShell or Command Prompt on your computer.

3. **Build Docker Image:**
   - Navigate to the directory containing your Dockerfile.
   - Run the following command to build the Docker image:
     ```
     docker build -t web-extractor .
     ```

4. **Run Docker Container:**
   - Run the following command to execute the Docker container and provide input via stdin:
     ```
     Get-Content input_file.txt | docker run -i web-extractor
     ```
     or

     ```
     type input.txt | docker run -i web-scraper
     ```

### Linux & macOS

1. **Install Docker:**
   - Install Docker Engine by following the instructions for [Linux](https://docs.docker.com/engine/install/) or [macOS](https://docs.docker.com/docker-for-mac/install/).

2. **Open Terminal:**
   - Open Terminal on your computer.

3. **Build Docker Image:**
   - Navigate to the directory containing your Dockerfile.
   - Run the following command to build the Docker image:
     ```
     docker build -t web-extractor .
     ```

4. **Run Docker Container:**
   - Run the following command to execute the Docker container and provide input via stdin:
     ```
     cat input_file.txt | docker run -i web-extractor
     ```

## Notes

- Replace `input_file.txt` with the name of the file containing the input you want to pass to your command-line application via stdin.
