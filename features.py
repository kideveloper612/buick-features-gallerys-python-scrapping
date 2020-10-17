import requests
from bs4 import BeautifulSoup


def request(url):
    res = requests.get(url)
    return res


def parse(content):
    return BeautifulSoup(content, 'html5lib')


def main():
    url = 'https://www.buick.com/suvs/encore'
    response = request(url)
    soup = parse(response.text)
    title_soups = soup.select('.q-margin-base.q-headline .medium-margin .q-headline3')
    for title_soup in title_soups:
        title = title_soup.text.strip()

        '.q-margin-base .q-text.q-body1 p'
        print(title_soup)


if __name__ == '__main__':
    main()
