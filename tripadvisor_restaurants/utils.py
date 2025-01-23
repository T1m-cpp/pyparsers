import csv
from bs4 import BeautifulSoup as bs
import requests
from rest import Restaurant 


cookies = {
    'TADCID': '-i_kuF2FY3wADVtdABQCrj-Ib21-TgWwDB4AzTFpg4MgxSr0YA6I09KMNbh5jsvJOcLIvrFwIY_nqYOXFhLJ5YWjDPzclgULDsk',
    'TASameSite': '1',
    'TAUnique': '%1%enc%3AO1EVIY11qCkNFGJVRjeG7nTpC1hFG%2BH8BYnWvNfIfwejkKkURl8XgPZIf1qx%2Bux9Nox8JbUSTxk%3D',
    'datadome': 'ZYJ1HDXuwBfxFYvekWcOjhPBz7VAbT42x5PeJU9EvfIc6zix2D548wkOCobGq2FR_kfDWNKgIHTv4KJSPqD3DG18qvjv9DjTqo99YE8k_CnEVSfFYzOP5QSu4cTw~29O',
    'TASession': 'V2ID.24B6E5E480C44900878D5CEF043E3672*SQ.146*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.ru*FA.1*DF.0*FLO.4049313*TRA.true*LD.303631*EAU._',
    'TASSK': 'enc%3AAK747997wxQix8JXIipd5NFOhv%2Fm2vn43f%2Ft4BfBXA6nhljX4ePVS0nHEieJyYqT%2FzYNmYQuKAxO18vvrdna9PiwCj%2FKGd5FUdeW8Vs7Xfn36sv195M%2FVtwswQkXgU%2F0qw%3D%3D',
    'PAC': 'AJBjW8u527xu8EIlSgvsBBbbzQM4jN-ddvo1nDONn0ZwiRn2NWr6BHiCHp3q3baBrYkXyvOkyLbcw-mDsrdoK-e5R4TsD4MMvumojX-pPzrP2mDru9qcjtnrT5vfmvYp0yR1-2NzukPcoBv9XwrzI0BMYW0MTA4yscFfGIz2Rrb4DuGn7oT6mDPGSwzEh4uideEcfb0tHzgK6w3ZvmkYc-tYvlt0tvx2-tWSP1PBBOL2pC5qNGSu133nMomGC5Sl7VQKwnmW1scNiuBFFB5gBUU%3D',
    'VRMCID': '%1%V1*id.10568*llp.%2FTourism-g293736-Rabat_Rabat_Sale_Kenitra-Vacations%5C.html*e.1738223080652',
    'TART': '%1%enc%3AFTXPeahhma%2BitZ0QpBUhmEHecjEclMzZApnyDa6hORdPdq1O1hEXFbHD7sKNy80cNox8JbUSTxk%3D',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Jan+23+2025+14%3A39%3A08+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=98b8aed3-7a23-43db-af46-1fcf075507e7&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'TATrkConsent': 'eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9',
    '_gcl_aw': 'GCL.1737632350.null',
    '_gcl_au': '1.1.1054193695.1737551749',
    '_ga_QX0Q50ZC9P': 'GS1.1.1737632215.5.1.1737632349.7.0.0',
    '_ga': 'GA1.1.1459939634.1737551749',
    'ServerPool': 'X',
    'PMC': 'V2*MS.91*MD.20250122*LD.20250123',
    'TATravelInfo': 'V2*A.2*MG.-1*HP.2*FL.3*RS.1',
    'TAUD': 'LA-1737541067428-1*RDD-1-2025_01_22*ARC-91359522*LG-91394832-2.1.F.*LD-91394833-.....',
    'TAReturnTo': '%1%%2FShowUserReviews-g3316797-d4049313-r876386480-Rabati_Castle-Akhaltsikhe_Samtskhe_Javakheti_Region.html',
    '_ym_uid': '1737617591526466794',
    '_ym_d': '1737617591',
    '_ym_isad': '2',
    '__vt': 'ohNFXwD5i6B6wB9FABQCT24E-H_BQo6gx1APGQJPtzL-h3xMhrGIxHhDafGH-Ew9gs7OSkVDtQzf3pjnoGoogGLWQr2acKMU01z_Ad3-CWCt5HbeZHEpsv4ZGYNIJ8d-c1y2IBV7EOTprYN8K0iktIvoaA',
    'TASID': '24B6E5E480C44900878D5CEF043E3672',
    'SRT': 'TART_SYNC',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.tripadvisor.ru/Restaurants-g303631-Sao_Paulo_State_of_Sao_Paulo.html',
    'Connection': 'keep-alive',
    # 'Cookie': 'TADCID=-i_kuF2FY3wADVtdABQCrj-Ib21-TgWwDB4AzTFpg4MgxSr0YA6I09KMNbh5jsvJOcLIvrFwIY_nqYOXFhLJ5YWjDPzclgULDsk; TASameSite=1; TAUnique=%1%enc%3AO1EVIY11qCkNFGJVRjeG7nTpC1hFG%2BH8BYnWvNfIfwejkKkURl8XgPZIf1qx%2Bux9Nox8JbUSTxk%3D; datadome=ZYJ1HDXuwBfxFYvekWcOjhPBz7VAbT42x5PeJU9EvfIc6zix2D548wkOCobGq2FR_kfDWNKgIHTv4KJSPqD3DG18qvjv9DjTqo99YE8k_CnEVSfFYzOP5QSu4cTw~29O; TASession=V2ID.24B6E5E480C44900878D5CEF043E3672*SQ.146*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.ru*FA.1*DF.0*FLO.4049313*TRA.true*LD.303631*EAU._; TASSK=enc%3AAK747997wxQix8JXIipd5NFOhv%2Fm2vn43f%2Ft4BfBXA6nhljX4ePVS0nHEieJyYqT%2FzYNmYQuKAxO18vvrdna9PiwCj%2FKGd5FUdeW8Vs7Xfn36sv195M%2FVtwswQkXgU%2F0qw%3D%3D; PAC=AJBjW8u527xu8EIlSgvsBBbbzQM4jN-ddvo1nDONn0ZwiRn2NWr6BHiCHp3q3baBrYkXyvOkyLbcw-mDsrdoK-e5R4TsD4MMvumojX-pPzrP2mDru9qcjtnrT5vfmvYp0yR1-2NzukPcoBv9XwrzI0BMYW0MTA4yscFfGIz2Rrb4DuGn7oT6mDPGSwzEh4uideEcfb0tHzgK6w3ZvmkYc-tYvlt0tvx2-tWSP1PBBOL2pC5qNGSu133nMomGC5Sl7VQKwnmW1scNiuBFFB5gBUU%3D; VRMCID=%1%V1*id.10568*llp.%2FTourism-g293736-Rabat_Rabat_Sale_Kenitra-Vacations%5C.html*e.1738223080652; TART=%1%enc%3AFTXPeahhma%2BitZ0QpBUhmEHecjEclMzZApnyDa6hORdPdq1O1hEXFbHD7sKNy80cNox8JbUSTxk%3D; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jan+23+2025+14%3A39%3A08+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=98b8aed3-7a23-43db-af46-1fcf075507e7&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; _gcl_aw=GCL.1737632350.null; _gcl_au=1.1.1054193695.1737551749; _ga_QX0Q50ZC9P=GS1.1.1737632215.5.1.1737632349.7.0.0; _ga=GA1.1.1459939634.1737551749; ServerPool=X; PMC=V2*MS.91*MD.20250122*LD.20250123; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUD=LA-1737541067428-1*RDD-1-2025_01_22*ARC-91359522*LG-91394832-2.1.F.*LD-91394833-.....; TAReturnTo=%1%%2FShowUserReviews-g3316797-d4049313-r876386480-Rabati_Castle-Akhaltsikhe_Samtskhe_Javakheti_Region.html; _ym_uid=1737617591526466794; _ym_d=1737617591; _ym_isad=2; __vt=ohNFXwD5i6B6wB9FABQCT24E-H_BQo6gx1APGQJPtzL-h3xMhrGIxHhDafGH-Ew9gs7OSkVDtQzf3pjnoGoogGLWQr2acKMU01z_Ad3-CWCt5HbeZHEpsv4ZGYNIJ8d-c1y2IBV7EOTprYN8K0iktIvoaA; TASID=24B6E5E480C44900878D5CEF043E3672; SRT=TART_SYNC',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def getRestLinks():
    offset = 0
    links = list()

    while True:
        print(offset)
        url = f"https://www.tripadvisor.ru/Restaurants-g303631-oa{str(offset)}-Sao_Paulo_State_of_Sao_Paulo.html"

        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
        )

        if response.status_code != 200:
            print(f"Failed to retrieve page with offset {offset}. Status code: {response.status_code}")
            break

        soup = bs(response.text, 'html.parser')

        divs = soup.find_all('div', class_="mfKvs f e")
        if len(divs) == 0:
            break


        for i in divs:
            link = i.find('a', class_ = "BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS")
            links.append("https://www.tripadvisor.ru/" + link['href'])
            print(link['href'])

        offset += 30  # Move to the next page


    links = list(set(links))

    with open('links.txt', 'w') as file:
        for link in links:
            file.write(link + '\n')  # Записываем каждую ссылку в новую строку

    print(f'Найдено {len(links)} ссылок. Ссылки сохранены в файл links.txt.')



    # считываем текст HTML-документа
  
def readLinksFromFile(file_path):
    links = []  # Список для хранения ссылок
    try:
        with open(file_path, 'r') as file:
            for line in file:
                link = line.strip()  # Убираем пробелы и символы новой строки
                if link:  # Проверяем, что строка не пустая
                    links.append(link)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except IOError:
        print(f"Ошибка при чтении файла '{file_path}'.")
    
    return links

def getRests():
    links = readLinksFromFile("links.txt")

    rests = list()
    cnt = 1

    for i in links:
        response = requests.get(
        i,
        cookies=cookies,
        headers=headers,
    )

        print(cnt, i)

        if response.status_code != 200:
            print("error")

        soup = bs(response.text, 'html.parser')

        tmp_name = soup.find('h1', class_="biGQs _P hzzSG rRtyp")
        name = tmp_name.text if tmp_name != None else "-"

        rating = soup.find('div', class_="jKCQq")
        if rating != None:
            rating = rating.find('title').text
        else:
            rating = "-"

        reviews_count= soup.find('span', class_="OFtgC")
        if reviews_count != None:
            reviews_count = reviews_count.text
        else:
            reviews_count = "-"
        
        print(reviews_count)


        tmp_address = soup.find('div', class_="YeQzG f Q3").find('div', class_= "biGQs _P fiohW fOtGX")
        address = tmp_address.text if tmp_address != None else "-"

        phone = soup.find('div', class_="PdyTq u _e q Q3 csvMt SBILQ") 
        if phone != None:
            phone = phone.find('span', class_="ALcKn").findPrevious().text
        else:
            phone = "-"

        tmp_cuisines = soup.find('div', class_='jKCQq')

        if tmp_cuisines != None:
            tmp_cuisines = tmp_cuisines.find('span', class_="abxVl VdWAl")
            cuisines = tmp_cuisines.text if tmp_cuisines != None else "-"
        else:
            tmp_cuisines = "-"

        #cuisines = tmp_cuisines.text if tmp_cuisines != None else "-"

        rests.append(Restaurant(name,rating,reviews_count,address,phone, cuisines))
        cnt += 1

    return rests

def save_restaurants_to_csv(restaurants, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Рейтинг','Количество отзывов', 'Адрес','Телефон', 'Категории'])  # Записываем заголовки
        for restaurant in restaurants:
            writer.writerow([restaurant.name, restaurant.rating,restaurant.reviews_count,restaurant.address,restaurant.phone, restaurant.cuisines])  # Записываем данные 

def main():
    #getRestLinks()
    rests = getRests()
    save_restaurants_to_csv(rests, "SaoPaulo/SaoPaulo.csv")

if __name__=="__main__":
    main()