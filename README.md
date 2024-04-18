# Pasquali Code Challange

Clone the repository

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
