#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import csv
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--ignore-certificate-errors')


driver = webdriver.Chrome(options=chrome_options)

def write_lists_to_csv_with_header(list_a, list_b, csv_file_name):
    # Combine the lists using zip
    combined_lists = list(zip(list_a, list_b))

    # Specify the header
    header = ['Class', 'Text']

    # Write the combined lists to a CSV file with two columns and a header
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        # Write the header
        csv_writer.writerow(header)

        # Write the data
        csv_writer.writerows(combined_lists)

    print(f'CSV file "{csv_file_name}" has been created.')


def get_mehrnews():

    list_of_sub_link = []
    text_list = []

    # -----------------------Culture-----------------------
    for i in range(1,10):
        link = f'https://www.mehrnews.com/page/archive.xhtml?mn=11&wide=0&dy=16&ms=0&pi={i}&yr=1402&tp=69'
        driver.get(link)
        # Improved selector to directly target the container holding the news links
        urls_div = driver.find_elements(By.CSS_SELECTOR, '.col-12.col-sm-8 a')
        list_of_sub_link = set(list_of_sub_link)
        for link in urls_div:
            if len(list_of_sub_link) < 100:
                href = link.get_attribute('href')
                # Ensure the href attribute is not None and is a valid URL before appending
                if href and href.startswith('https://www.mehrnews.com/news/'):
                    list_of_sub_link.add(href)
            else:
                break

    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body').text
            if str(a) != '':
                text_list.append(str(a))
        except:
            pass
    write_lists_to_csv_with_header(['culture']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/mehrnews/culture.csv')

    list_of_sub_link = []
    text_list = []

    #-----------------------Politics-----------------------
    for i in range(1,10):
        link = f'https://www.mehrnews.com/page/archive.xhtml?mn=11&wide=0&dy=16&ms=0&pi={i}&yr=1402&tp=7'
        driver.get(link)
        # Improved selector to directly target the container holding the news links
        urls_div = driver.find_elements(By.CSS_SELECTOR, '.col-12.col-sm-8 a')
        list_of_sub_link = set(list_of_sub_link)
        for link in urls_div:
            if len(list_of_sub_link) < 100:
                href = link.get_attribute('href')
                # Ensure the href attribute is not None and is a valid URL before appending
                if href and href.startswith('https://www.mehrnews.com/news/'):
                    list_of_sub_link.add(href)
            else:
                break

    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body').text
            if str(a) != '':
                text_list.append(str(a))
        except:
            pass
    write_lists_to_csv_with_header(['politics']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/mehrnews/politics.csv')

    list_of_sub_link = []
    text_list = []

    #-----------------------Sport-----------------------
    for i in range(1,10):
        link = f'https://www.mehrnews.com/page/archive.xhtml?mn=11&wide=0&dy=16&ms=0&pi={i}&yr=1402&tp=9'
        driver.get(link)
        # Improved selector to directly target the container holding the news links
        urls_div = driver.find_elements(By.CSS_SELECTOR, '.col-12.col-sm-8 a')
        list_of_sub_link = set(list_of_sub_link)
        for link in urls_div:
            if len(list_of_sub_link) < 100:
                href = link.get_attribute('href')
                # Ensure the href attribute is not None and is a valid URL before appending
                if href and href.startswith('https://www.mehrnews.com/news/'):
                    list_of_sub_link.add(href)
            else:
                break

    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body').text
            if str(a) != '':
                text_list.append(str(a))
        except:
            pass
    write_lists_to_csv_with_header(['sport']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/mehrnews/sport.csv')

    list_of_sub_link = []
    text_list = []

    #-----------------------Economy-----------------------
    for i in range(1,10):
        link = f'https://www.mehrnews.com/page/archive.xhtml?mn=11&wide=0&dy=16&ms=0&pi={i}&yr=1402&tp=25'
        driver.get(link)
        # Improved selector to directly target the container holding the news links
        urls_div = driver.find_elements(By.CSS_SELECTOR, '.col-12.col-sm-8 a')
        list_of_sub_link = set(list_of_sub_link)
        for link in urls_div:
            if len(list_of_sub_link) < 100:
                href = link.get_attribute('href')
                # Ensure the href attribute is not None and is a valid URL before appending
                if href and href.startswith('https://www.mehrnews.com/news/'):
                    list_of_sub_link.add(href)
            else:
                break

    for j, i in enumerate(list_of_sub_link):
        print(f"Getting Link: {i}")
        try:
            driver.get(i)
            a = driver.find_element(By.CLASS_NAME, 'item-body').text
            if str(a) != '':
                text_list.append(str(a))
        except:
            pass
    write_lists_to_csv_with_header(['economy']*len(text_list), text_list, csv_file_name= f'{os.path.dirname(__file__)}/mehrnews/economy.csv')

def create_folder(folder_name, name):
    folder_name += f'/{name}' 
    try:
        # Create a folder in the current working directory
        os.mkdir(folder_name)
        print(f'Folder "{folder_name}" created successfully.')
    except FileExistsError:
        print(f'Folder "{folder_name}" already exists.')

create_folder(os.path.dirname(__file__), 'mehrnews')

get_mehrnews()
