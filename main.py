import time
import requests
import lxml
import os
import csv
from transliterate import translit

from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36'
    }

    #1) получение каждой страницы из 9

    # for i in range(1, 10):
    #     url = f'https://www.etm.ru/catalog?searchValue=%D0%9A%D0%BE%D1%82%D0%B5%D0%BB+%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9+&page={i}&rows=12'
    #     r = requests.get(url=url, headers=headers)
    #     with open(f'pages/page_{i}.html', 'w', encoding='utf-8') as file:
    #         file.write(r.text)
    #     print('прошел')
    #
    #     time.sleep(2)

    # 2) создаем папки для карточек
    # for i in range(1, 10):
    #     if not os.path.exists(f'page_cards{i}'):
    #         os.mkdir(f'pages/page_cards{i}')


    # запись каждого товара в папки
    # for i in range(1, 10):
    #     url = f'https://www.etm.ru/catalog?searchValue=%D0%9D%D0%B0%D1%81%D0%BE%D1%81%D1%8B+%D0%B1%D1%8B%D1%82%D0%BE%D0%B2%D1%8B%D0%B5&page={i}&rows=12'
    #     r = requests.get(url=url, headers=headers)
    #     src = r.text
    #
    #     soup = BeautifulSoup(src, 'lxml')
    #     items =soup.find_all('div', class_='jss162')
    #     # print(items)
    #
    #
    #     cifra = 0
    #     for item in items:
    #         link_by_item = 'https://www.etm.ru/' + item.find('div', class_='jss178').find('a').get('href')
    #         print(link_by_item)
    #         cifra += 1
    #
    #         r = requests.get(url=link_by_item, headers=headers)
    #         with open(f'pages/page_cards{i}/card{cifra}.html', 'w', encoding='utf-8') as file:
    #             file.write(r.text)
    #
    #         time.sleep(10)
    #
    #
    #     print('=====================')


def get_main_data():
    id_item = 100
    with open('elektro.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
            ['id_item', 'name_item', 'picture', 'engName_item', 'kod_item', 'proreties', 'val_properties', 'rozn_price', 'your_price', 'descr', 'kateg1', 'kateg2']
        )
    for count in range(1, 10):
        print(f'({count})')
        for cards in os.listdir(f'pages/page_cards{count}'):
            # print(cards)

            with open(f'pages/page_cards{count}/{cards}', 'r', encoding='utf-8') as file:
                src = file.read()

            soup = BeautifulSoup(src, 'lxml')

            id_item += 1
            #поиск всех элементов

            name = soup.find('h1', 'jss115').text
            picture = soup.find('div', 'jss49').find('img').get('src')
            eng_name = soup.find('h1', 'jss115').text
            eng_name = translit(eng_name, language_code='ru', reversed=True)
            kod_item = soup.find('p', class_='jss127').text

            clas = soup.find('p', class_='jss162')
            country = clas.nextSibling
            proizvod = country.nextSibling
            articul = proizvod.nextSibling
            articul_rasshiren = articul.nextSibling
            # ед измерения
            try:
                prop1 = articul_rasshiren.nextSibling
            except:
                prop1 = 'пусто:пусто'
            try:
                prop2 = prop1.nextSibling
            except:
                prop2 = 'пусто:пусто'
            try:
                prop3 = prop2.nextSibling
            except:
                prop3 = 'пусто:пусто'


            try:
                type_izdelia = soup.find_all('div', 'jss161')[1].next_element
            except:
                type_izdelia = 'пусто:пусто'
            try:
                prop4 = type_izdelia.nextSibling
            except:
                prop4 = 'пусто:пусто'
            try:
                prop5 = prop4.nextSibling
            except:
                prop5 = 'пусто:пусто'
            try:
                prop6 = prop5.nextSibling
            except:
                prop6 = 'пусто:пусто'
            try:
                prop7 = prop6.nextSibling
            except:
                prop7 = 'пусто:пусто'
            try:
                prop8 = prop7.nextSibling
            except:
                prop8 = 'пусто:пусто'
            try:
                prop9 = prop8.nextSibling
            except:
                prop9 = 'пусто:пусто'
            try:
                prop10 = prop9.nextSibling
            except:
                prop10 = 'пусто:пусто'


            try:
                rozn_price = soup.find_all('p', 'jss144')[0]
            except:
                rozn_price = 'пусто:пусто'
            try:
                vasha_price = soup.find_all('p', 'jss144')[1]
            except:
                vasha_price = 'пусто:пусто'
            try:
                descr = soup.find('p', 'jss58')
            except:
                descr = 'пусто:пусто'
            try:
                kateg1 = soup.find('div', 'jss111').text.split('/')[-2].strip()
            except:
                kateg1 = 'пусто:пусто'
            try:
                kateg2 = soup.find('div', 'jss111').text.split('/')[-1].strip()
            except:
                kateg2 = 'пусто:пусто'



            #приведение всех эдементов к тексту
            clas = clas.text
            country = country.text
            proizvod = proizvod.text
            articul = articul.text
            articul_rasshiren = articul_rasshiren.text

            try:
                prop1 = prop1.text
            except AttributeError:
                prop1 = 'пусто:пусто'
            try:
                prop2 = prop2.text
            except AttributeError:
                prop2 = 'пусто:пусто'
            try:
                prop3 = prop3.text
            except AttributeError:
                prop3 = 'пусто:пусто'
            try:
                type_izdelia = type_izdelia.text
            except AttributeError:
                type_izdelia = 'пусто:пусто'
            try:
                prop4 = prop4.text
            except AttributeError:
                prop4 = 'пусто:пусто'
            try:
                prop5 = prop5.text
            except AttributeError:
                prop5 = 'пусто:пусто'
            try:
                prop6 = prop6.text
            except AttributeError:
                prop6 = 'пусто:пусто'
            try:
                prop7 = prop7.text
            except AttributeError:
                prop7 = 'пусто:пусто'
            try:
                prop8 = prop8.text
            except AttributeError:
                prop8 = 'пусто:пусто'
            try:
                prop9 = prop9.text
            except AttributeError:
                prop9 = 'пусто:пусто'
            try:
                prop10 = prop10.text
            except AttributeError:
                prop10 = 'пусто:пусто'

            try:
                rozn_price = rozn_price.text
            except:
                rozn_price = 'нетцены:нетцены'
            try:
                vasha_price = vasha_price.text
            except:
                vasha_price = 'нетцены:нетцены'
            try:
                descr = descr.text
            except:
                descr = 'пусто:пусто'


            dannie = [
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), clas.split(':')[0],
                 clas.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), country.split(':')[0],
                 country.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), proizvod.split(':')[0],
                 proizvod.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), articul.split(':')[0],
                 articul.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), articul_rasshiren.split(':')[0],
                 articul_rasshiren.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop1.split(':')[0],
                 prop1.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop2.split(':')[0],
                 prop2.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop3.split(':')[0],
                 prop3.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), type_izdelia.split(':')[0],
                 type_izdelia.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop4.split(':')[0],
                 prop4.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop5.split(':')[0],
                 prop5.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop6.split(':')[0],
                 prop6.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop7.split(':')[0],
                 prop7.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop8.split(':')[0],
                 prop8.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop9.split(':')[0],
                 prop9.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                [id_item, name, picture, eng_name, kod_item.split(':')[-1].strip(), prop10.split(':')[0],
                 prop10.split(':')[-1], rozn_price, vasha_price, descr, kateg1, kateg2],
                ]

            for val in dannie:
                with open('elektro.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        val
                    )





            print(cards)
            print(kateg2)
            print(kateg1)
            print('================')


        print('=============')






def main():
    get_data('https://www.etm.ru/catalog?searchValue=%D0%9D%D0%B0%D1%81%D0%BE%D1%81%D1%8B+%D0%B1%D1%8B%D1%82%D0%BE%D0%B2%D1%8B%D0%B5&page=1&rows=12')
    get_main_data()

if __name__ == '__main__':
    main()
