import pygame
import requests
import sys
import os
pygame.init()
size = 750, 750
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
pygame.display.flip()
running = True
coords = (11.13414, 042.235235)
scale = float(0.1223)

def show_map(coord=None, spn=None, map_type="map", add_params=None):
    if coord and spn:
        map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l={}".format(coord[0], coord[1], spn, spn, map_type)
    else:
        map_request = "http://static-maps.yandex.ru/1.x/?l={map_type}".format(**locals())

    if add_params:
        map_request += "&" + add_params
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)

show_map(coords, scale, 'map')
current_picture = pygame.image.load('map.png')
current_picture = pygame.transform.scale(current_picture, (750, 750))
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(current_picture, (0, 0))
    pygame.display.flip()
pygame.quit()