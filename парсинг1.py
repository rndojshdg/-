import requests

from bs4 import BeautifulSoup

import os



# URL страницы, которую хотим спарсить

url = ""  # Замените на URL, который вам интересен



# Отправляем запрос к серверу и получаем содержимое страницы

response = requests.get(url)



# Проверяем, что запрос был успешным (HTTP-код 200)

if response.status_code == 200:

    # Используем BeautifulSoup для анализа HTML-кода

    soup = BeautifulSoup(response.content, "html.parser")



    # Найдем все изображения на странице

    images = soup.find_all("img")



    # Указываем абсолютный путь к папке для сохранения изображений

    save_folder = "C:/Users/Пользователь/Desktop/парсингсайта"  # Замените на свой путь



    # Проверяем, существует ли указанная папка, и создаем ее, если нет

    if not os.path.exists(save_folder):

        os.makedirs(save_folder)



    # Счетчик для именования изображений

    count = 1



    # Сохраняем изображения

    for img in images:

        img_url = img.get("src")

        if img_url:

            img_response = requests.get(img_url)

            if img_response.status_code == 200:

                # Имя файла: image1.jpg, image2.jpg, и т.д.

                filename = f"image{count}.jpg"

                file_path = os.path.join(save_folder, filename)

                

                # Сохраняем изображение в бинарном режиме

                with open(file_path, "wb") as img_file:

                    img_file.write(img_response.content)

                    print(f"Изображение {count} сохранено в {file_path}")

                    count += 1

else:

    print("Ошибка при получении страницы:", response.status_code)

