import requests
from bs4 import BeautifulSoup

url = "http://example.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the title tag
    title_tag = soup.find("title")

    # Check if the title tag was found and print its content
    if title_tag:
        print("Title of the website:", title_tag.text)
    else:
        print("Title tag not found in the HTML content.")
else:
    print(
        f"Failed to fetch the content. HTTP status code: {response.status_code}")

