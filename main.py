import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


SMTP_ADDRESS = "smtp.gmail.com"
GMAIL = "XXXX"
PASSWORD = "XXXX"

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent":"XXXX",
    "Accept-Language": "XXXX"
}
response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.text, "lxml")

title_1 = soup.find('span', id='productTitle')
if title_1:
    title = title_1.get_text().strip()
    print(title)

price_span = soup.find('span', class_='a-offscreen')
if price_span:
    price = float(price_span.get_text().split("$")[1])
    print(price)

BUY = 200

if price < BUY:
    message = f"{title} is now {price}"
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(GMAIL, PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=GMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )