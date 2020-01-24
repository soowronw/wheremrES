import json
import requests
geocode = 'https://geocode-maps.yandex.ru/1.x/?apikey=ВАШ АПИ ключ&format=json&geocode='
with open(r'D:\PycharmProjects\parsingHouseMoscow\moscow_buildings.json', 'r', encoding='utf-8') as json_file:
    data = json.loads(json_file.read())
    filejs = open('houses.js', 'a')
    for row in data["rows"]:
        try:
            if (row["area_name"] == "муниципальный округ Хамовники") or \
                    (row["area_name"] == "муниципальный округ Якиманка") or \
                    (row["area_name"] == "муниципальный округ Гагаринский") or \
                    (row["area_name"] == "муниципальный округ Академический") or \
                    (row["area_name"] == "муниципальный округ Донской") and \
                    (1956 <= int(row["house_year"]) < 1989):
                new_address = row["full_address"].replace(' ', '+')
                geocode1 = geocode + new_address
                response = requests.get(geocode1)
                output = json.loads(response.content)
                coordinates = output['response']["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]['pos']
                eastern_longitude, northern_latitude = coordinates.split(' ')
                print('.add(new ymaps.Placemark([{},{}]))'.format(northern_latitude, eastern_longitude))
                filejs.write('.add(new ymaps.Placemark([{},{}]))'.format(northern_latitude, eastern_longitude) + '\n')
        except Exception as e:
            pass
    filejs.write('}')
    filejs.close()