import pprint

from ultralytics import YOLO
import os
from object_sort import object_sort
from pymongo import MongoClient


def detect(diction):
    i = 0
    fds = os.listdir(f'src/{diction}')
    for img in fds:
        model.predict(f'src/{diction}/' + img, save=True, save_txt=True, imgsz=640, conf=0.6)
        i += 1
        print(f'{i} изображение обработано')


def or_search(x):
    print(f'Функция или, {x} - числа')


def and_search(x):
    print(f'Функция и, {x} - числа')


def choose(n=0):
    func = {
        '|': lambda x: or_search(x),
        '&': lambda x: and_search(x)
    }
    digits = list()
    symbol = list()
    list_with_collections = list(db.list_collection_names())
    list_with_collections.remove('already_processed')
    print("Доступные классы для выбора:")
    for index, cls in enumerate(list_with_collections):
        print(index, cls)

    print("Для выхода, введите exit/quit, или выберите номер класса")
    n = input("Выбор может быть одиночным или комбинацией 2 классов: ")
    print()

    # | - или
    # & - и

    if n == "exit" or n == "quit":
        return

    for i in n.split():
        if i.isdigit():
            digits.append(i)
        else:
            symbol.append(i)

    if len(symbol) == 0:
        try:
            for coll in db[list_with_collections[int(n)]].find():
                print(f'name: {coll["name"]}')
                print(f'time: {coll["time"]}\n')
            choose()
        except ValueError:
            print("Неверно выбран номер класса")
            choose()
    elif len(digits) == 0:
        print("Отсутствуют номера классов в запросе, попробуйте ещё раз")
        choose()

    elif symbol[0] == '|' or symbol[0] == '&':
        func[symbol[0]](digits)
    else:
        print("Неверная команда")
        choose()


if __name__ == '__main__':
    client = MongoClient("mongodb://localhost:27017/")
    db = client["video_base"]

    model = YOLO('yolov8n.pt')
    dictionary = os.listdir("src/")
    count = 0
    print("Проверка видео на обработанность...")
    for d in dictionary:
        if not db['already_processed'].find_one({"name": f'{d}'}):
            detect(d)
            object_sort(d)
            count += 1
            db['already_processed'].insert_one({"name": f'{d}'})
            print(f'{count} видео обработано')
    print("Все видео прошли проверку...")
    choose()
