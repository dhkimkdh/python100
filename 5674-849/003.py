import requests
from bs4 import BeautifulSoup

urls = ["https://www.naver.com/", "https://www.python.org/"]
filename= "robots.txt"

for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")
    
    """
    html_src = resp.text
    soup = BeautifulSoup(html_src, 'html.parser')
    f_text = soup.find('Disallow:')
    print(f_text)
    """

    