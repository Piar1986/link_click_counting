import argparse
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def create_parser():
    parser = argparse.ArgumentParser(description='Сокращение ссылок с помощью Bitly')
    parser.add_argument('user_input', help='Адрес ссылки')
    return parser

def shorten_link(token, url):
  header = { 'Authorization': token }
  payload = { "long_url": url}
  response = requests.post(shorten_url_template, json=payload, headers=header)
  response.raise_for_status()
  bitlink = response.json()['link']
  return bitlink

def count_clicks(token, link):
  header = { 'Authorization': token }
  total_click_url = total_click_url_template.format(link)
  response = requests.get(total_click_url, headers=header, params = {'units':'-1'})
  response.raise_for_status()
  clicks_count = response.json()['total_clicks']
  return clicks_count

if __name__ == '__main__':
  access_token = os.getenv("ACCESS_TOKEN")
  total_click_url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
  shorten_url_template = 'https://api-ssl.bitly.com/v4/shorten'

  parser = create_parser()
  args = parser.parse_args()

  if args.user_input.startswith("bit.ly/", 0, 7):
    try:
      clicks_count = count_clicks(access_token, args.user_input)
      print('Сумма кликов по битлинку за все время:', clicks_count)
    except requests.exceptions.HTTPError:
      print('Не найден битлинк:', args.user_input)    
  else:
    try:
      bitlink = shorten_link(access_token, args.user_input)
      print('Короткая ссылка:', bitlink)
    except requests.exceptions.HTTPError:
      print('Не найдена введенная ссылка:', args.user_input)