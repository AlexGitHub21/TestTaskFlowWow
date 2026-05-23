import requests
import json
import pandas as pd
import logging
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('EXCHANGE_API_KEY')

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
try:
    logging.info("Отправка запроса к API")
    response = requests.get(url)
    data = response.json()

    logging.info("Данные успешно получены")

    with open('backup.json', 'w') as f:
        json.dump(data, f, indent=4)

    logging.info("Данные в JSON сохранены")

    rates = data['conversion_rates']

    colNames = ["Currency", "Rate_to_USD"]
    df = pd.DataFrame(rates.items(), columns=colNames)
    df.to_csv('rates.csv', index=False, encoding='utf-8')

    df.to_excel('rates.xlsx', index=False)

    logging.info("Курсы валют сохранены в csv, xlsx")

except requests.exceptions.RequestException as e:
    logging.error(f'Ошибка API: {e}')

except Exception as e:
    logging.error(f'Ошибка: {e}')
