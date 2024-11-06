# pip install beautifulsoup4 -- Deze moet je runnen in de terminal ipv hier!


from bs4 import BeautifulSoup
import urllib.request

# Define the URL
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Open the URL and read the response
page = urllib.request.urlopen(url)
html_content = page.read().decode('utf-8')

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html')

# Print the parsed HTML content (optional)
# print(soup), 'html')

#print(soup)
