import pygame
import requests
import sys
import os
coords = [float(x) for x in input().split()]
scale = float(input())
pygame.init()
size = 750, 750
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
pygame.display.flip()
running = True

# coords = (11.13414, 042.235235)
# scale = float(0.1223)

def show_map(coord=None, spn=None, map_type="map", add_params=None):
    if coord and spn:
        map_request = "http://static-maps.yandex.ru/1.x/?ll={},{}&spn={},{}&l={}".format(coord[0], coord[1], spn, spn, map_type)
    else:
        map_request = "http://static-maps.yandex.ru/1.x/?l={map_type}".format(**locals())

    # if add_params:
    #     map_request += "&" + add_params
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

while running:
    show_map(coords, scale, 'map')
    current_picture = pygame.image.load('map.png')
    current_picture = pygame.transform.scale(current_picture, (750, 750))
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == 274:
                coords = (coords[0], max(coords[1] - scale, -180))
            if event.key == 273:
                coords = (coords[0], min(coords[1] + scale, 180))
            if event.key == 276:
                coords = (max(coords[0] - scale, -90), coords[1])
            if event.key == 275:
                coords = (min(coords[0] + scale, 90), coords[1])
    screen.blit(current_picture, (0, 0))
    pygame.display.flip()
pygame.quit()
#sdgjks;dg