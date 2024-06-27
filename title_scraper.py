import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    """
    Fetches the web page content from the provided URL and extracts all
    article titles from <h1> and <h2> tags.

    Parameters:
    url (str): The URL of the web page to scrape.

    Returns:
    list: A list of extracted titles.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        article_titles = [tag.get_text(strip=True) for tag in soup.find_all(["h1", "h2",])]
        return article_titles
    except requests.RequestException as error:
        print(f"Error fetching the URL: {error}")
        return []

def save_titles_to_file(titles, file_name):
    """
    Saves the list of titles to a text file, each title on a new line.

    Parameters:
    titles (list): The list of titles to save.
    file_name (str): The name of the file to save the titles in.
    """
    try:
        with open(file_name, "w") as file:
            for title in titles:
                file.write(title + "\n")
        print(f"Titles saved to {file_name}")
    except IOError as error:
        print(f"Error writing to file: {error}")

if __name__ == "__main__":
    url_to_scrape = input("Enter URL: ")
    output_file_name = "titles.txt"

    article_titles = scrape_titles(url_to_scrape)
    save_titles_to_file(article_titles, output_file_name)
