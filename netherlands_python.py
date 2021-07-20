import requests
from bs4 import BeautifulSoup
import boto3

base_url = "https://www.netherlandsandyou.nl/travel-and-residence/visas-for-the-netherlands"
sns = boto3.client('sns')

def lambda_handler(event, context):
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, "html.parser")
    info = soup.find(class_="intro").get_text()
    sns.publish(TopicArn='arn:aws:sns:eu-west-1:xxxxxxxxxxxxxx:netherlands',Message= "The info in the site today is: " +info)
    return
