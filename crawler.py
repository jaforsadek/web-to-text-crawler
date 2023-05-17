import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = 'https://www.techtarget.com/searchenterpriseai/definition/deep-learning-deep-neural-network'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_dom = response.content

# Create a Beautiful Soup object
soup = BeautifulSoup(html_dom, 'html.parser')

# Remove unnecessary images
for img in soup.find_all('img'):
    img.extract()

# Remove unnecessary links
for link in soup.find_all('a'):
    link.extract()

# Retrieve the modified HTML
modified_html = soup.prettify()

# Save the modified HTML as an HTML file
with open('modified.html', 'w', encoding='utf-8') as file:
    file.write(modified_html)

print("Modified HTML saved as modified.html")
