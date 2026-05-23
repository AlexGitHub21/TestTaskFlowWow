# TestTaskFlowWow

Скрипт получает курсы валют относительно USD через API ExchangeRate, сохраняет ответ в JSON, преобразует данные в DataFrame и экспортирует результат в CSV и XLSX

### 1. Клонирование репозитория
```bash
git clone https://github.com/AlexGitHub21/TestTaskFlowWow.git
cd TestTaskFlowWow
````

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Переменные окружения
Создать файл .env в папке проекта
Прописать в файле переменную `EXCHANGE_API_KEY={API KEY}`

### 4. Запуск скрипта
```commandline
python main.py
```

### Результат работы

После выполнения скрипта будут созданы или обновлены следующие файлы:

- `backup.json` — резервная копия ответа API в JSON-формате;
- `rates.csv` — таблица курсов валют в CSV;
- `rates.xlsx` — таблица курсов валют в Excel;
- `py_log.log` — файл логирования выполнения скрипта.