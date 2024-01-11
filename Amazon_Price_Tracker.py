import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "LINK OF PRODUCT ON AMAZON"
header = {
    "User-Agent": "Your User-Agent",
    "Accept-Language": "Your Accept-Language"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

YOUR_PASSWORD = 'App Password'
YOUR_EMAIL = 'Your Email'
YOUR_SMTP_ADDRESS = 'SMTP Email Address'

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_SMTP_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )


