# Обрезка ссылок с помощью Битли

Функционал:

1. Сокращение ссылки

   Пример команды запуска: 
   
   `python link_click_counting.py https://mail.ru`
   
   Результат выполнения:
   
   `Короткая ссылка: https://bit.ly/2XlinVl`

2. Определение количества переходов по сокращенной ссылке за все дни

   Пример команды запуска:
   
   `python link_click_counting.py bit.ly/2XlinVl`
   
   Результат выполнения: 
   
   `Сумма кликов по битлинку за все время: 2`


## Как установить

Для взаимодействия с API Bitly нужен персональный ключ - токен.

Зарегистрируйтесь на сайте [Bitly](https://bit.ly/)

Получите токен наподобие: `17c09e20ad155405123ac1977542fecf00231da7`

[Генератор токенов](https://bitly.com/a/oauth_apps)

`GENERIC ACCESS TOKEN — нужный тип токена`

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`


## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [Devman](https://dvmn.org).
