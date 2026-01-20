import requests


def get_moto_data_by_vin(vin):
    # Убираем пробелы, если юзер скопировал криво
    clean_vin = vin.strip()

    # API американского регулятора (бесплатный)
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{clean_vin}?format=json"

    try:
        response = requests.get(url, timeout=5)
        # Если API ответил не 200 (ОК), возвращаем пустоту
        if response.status_code != 200:
            return None

        data = response.json()

        # Ответ API очень большой, нам нужно найти конкретные поля в списке 'Results'
        results = data.get('Results', [])

        vehicle_info = {
            'year': None,
            'brand': None,
            'model': None
        }

        # Перебираем список характеристик
        for item in results:
            variable = item.get('Variable')
            value = item.get('Value')

            if variable == 'Model Year':
                vehicle_info['year'] = value
            elif variable == 'Make':  # Make = Brand
                vehicle_info['brand'] = value
            elif variable == 'Model':
                vehicle_info['model'] = value

        # Если не нашли даже Марку, считаем, что поиск не удался
        if not vehicle_info['brand']:
            return None

        return vehicle_info

    except Exception as e:
        print(f"Ошибка API: {e}")
        return None