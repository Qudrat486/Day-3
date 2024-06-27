# Title Scraper

This project is a simple Python script that scrapes article titles from a specified URL and saves them to a text file. The script extracts titles from `<h1>` and `<h2>` tags using the `requests` and `BeautifulSoup` libraries.

## Features

- Fetches web page content from a provided URL.
- Extracts article titles from `<h1>` and `<h2>` tags.
- Saves the extracted titles to a text file.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/title_scraper.git
    cd title_scraper
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```bash
    python title_scraper.py
    ```

2. Enter the URL you want to scrape when prompted:
    ```bash
    Enter URL: https://www.example.com
    ```

3. The titles will be saved to `titles.txt` in the same directory.

## Example

Here's an example of how to use the script:

```bash
$ python title_scraper.py
Enter URL: https://www.tutorialspoint.com/data_structures_algorithms/index.htm
Titles saved to titles.txt
```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
