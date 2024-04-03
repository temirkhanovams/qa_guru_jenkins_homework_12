# Подсказки по запуски тестов через консоль
- Запустить все тесты через консоль, если настроен pytest.ini
[pytest]

- Запустить все тесты, если в pytest.ini не указаны параметры папки и параметры удаления
[pytest --clean-alluredir --alluredir=allure-results]

- Сгенерировать allure-отчёт (локальный) - Windows в корне проекта в папке allure-results
[allure.bat serve allure-results]
