import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all('h2')

    with open("headlines.txt", "w", encoding="utf-8") as file:
        count = 1
        for headline in headlines:
            text = headline.get_text().strip()
            if text:
                print(f"{count}. {text}")
                file.write(f"{count}. {text}\n")
                count += 1

    print("\nHeadlines saved to 'headlines.txt'")
else:
    print(f"Failed to fetch page, Status code: {response.status_code}")

