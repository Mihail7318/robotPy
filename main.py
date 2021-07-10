import face_recognition
import numpy as np
import cv2
import os
import golos
import sintez

#cam = cv2.VideoCapture(0)  # Камера
names = []  # Словарь с именами


def face_rec(cam):
    flag = 0
    for i in range(30):
        cam.read()  # получить изображение с камеры
    ret, frame = cam.read()  # получить окончательное изображение
    print(face_recognition.face_locations(frame))  # Для отладки вывод сигнатуры фото
    if not face_recognition.face_locations(frame):  # Если лицо не распознано
        print("no_faces")
    else:
        face_encodings = face_recognition.face_encodings(frame)[0]  # декодировать первое найденое лицо
        count = 0  # счетчик лиц
        for filename in os.listdir('faces'):  # цикл перебора лиц
            if filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
                face = face_recognition.load_image_file('faces/' + filename)
                face_enc = face_recognition.face_encodings(face)[0]
                res = face_recognition.compare_faces([face_enc], face_encodings)
            if (res == [True]):
                golos.go("Здраствуйте " + names[count])
                golos.go("Разрешите замерить вашу температуру")
                flag = 1
                break
            count = count + 1
        if flag == 0:
            cv2.imwrite('faces/' + str(len(names) + 1) + '.jpg', frame)
            #golos.go("Здраствуйте. Как вас зовут?")
            name = sintez.go()
            names.append(str(name))
            adding()
            golos.go('Очень приятно ' + str(name))
            golos.go('Разрешите замерить вашу температуру')

    cam.release()


def adding():
    #names= ['Михаил']
    f = open('text.txt', 'w')
    for nam in names:
        f.write(nam + '\n')
    f.close()


def get():
    t = open('text.txt')
    while True:
        line = t.readline()
        if not line:
            break
        names.append(line.strip())
    t.close()


if __name__ == '__main__':
    get()
    #print(names)
    face_rec()
    adding()

def go(cam):
    get()
    #print(names)
    face_rec(cam)
    adding()