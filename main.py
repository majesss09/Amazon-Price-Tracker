import requests
from bs4 import BeautifulSoup
import smtplib
import dotenv
import os
dotenv.load_dotenv()

TARGET_PRICE = 300


response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

price_whole = int(soup.find("span", class_="a-price-whole").text.rstrip("."))
price_fraction = int(soup.find("span", class_="a-price-fraction").text.rstrip("."))
price = price_whole + price_fraction/100

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]
SMTP_ADDRESS= os.environ["SMTP_ADDRESS"]

if price < TARGET_PRICE:
    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=MY_EMAIL, 
                            msg=f"Subject:Amazon Price Alert!\n\nInstant Pot is now ${price}!\nhttps://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")



