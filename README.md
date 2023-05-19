# fast_api
## Установка 
``` cmd
git clone https://github.com/DeviTqq/fast_api.git
```

## Активация окружения
``` cmd
.\fapi\scripts\activate.bat
```
## Установка зависимостей 
``` cmd
pip install -r requirements.txt
```

## Создание DataBases в pgAdmin
![image](https://github.com/DeviTqq/fast_api/assets/95002224/f4702bba-aefa-41ec-b846-dcc3b34bcdbc)

![image](https://github.com/DeviTqq/fast_api/assets/95002224/20535b11-ee0c-47cf-a9b1-65cac0f27d7e)

## Запуск сервера
### Миграции
```cmd
alembic revision --autogenerate
alembic upgrade head
```

### Запуск
```cmd
uvicorn main:app --reload
```
