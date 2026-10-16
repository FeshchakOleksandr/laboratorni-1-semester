from bs4 import BeautifulSoup

def run_bs4():
    soup = BeautifulSoup("<b>Привіт світ</b>", "html.parser")
    print(soup.b.text)