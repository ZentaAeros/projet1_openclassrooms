import re
import requests
from bs4 import BeautifulSoup
import csv
import os
import urllib.request

""" Récupère toutes les informations d'un livre"""
def bookInfos(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    productDescription = soup.find_all('p')[3].text
    replaceDescription = productDescription.replace(',', '\,')
    universalProductCode = soup.find_all('td')[0].text
    priceIncludingTaxe = soup.find_all('td')[3].text[1:]
    priceExcludingTaxe = soup.find_all('td')[2].text[1:]
    numberAvailable = soup.find_all('td')[5].text[10:][:2]
    reviewRating = soup.find_all('td')[6].text
    title = soup.find('h1').text
    category = soup.find_all('a')[3].text
    sourceImage = 'http://books.toscrape.com' + soup.find('img')['src'][5:]
    link = response.url

    book_description = [replaceDescription, link, universalProductCode, title, priceIncludingTaxe, priceExcludingTaxe, numberAvailable, category, reviewRating, sourceImage]

    return book_description