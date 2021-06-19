import requests, smtplib, time
from bs4 import BeautifulSoup

URL = 'https://lenta.com/product/syrok-glazirovannyjj-byu-aleksandrov-v-molochnom-shokolade-kartoshka-rossiya-50g-260724/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', class_='sku-page__title').get_text().strip()
    price = soup.find('span', class_='price-label__integer').get_text().strip()

    if (price < 45):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('test@gmail.com', 'Your Less secure app password')
    subject = 'Сiрки Б.Ю. Александров по меньшей цене!'
    body = 'Смотри в магазине Лента! https://lenta.com/product/syrok-glazirovannyjj-byu-aleksandrov-v-molochnom-shokolade-kartoshka-rossiya-50g-260724/'

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail('from@gmail.com', 'to@gmail.com', message)
    server.quit()

while(True):
    check_price()
    time.sleep(86400) # Seconds in a day

