'''Разобьем фййл uszips.csv на много (68) по 500 строчек'''
import os
import shutil

from django.core.management import BaseCommand

filename = "uszips.csv"

filepath_1 = 'temp1'


def rm_r(path):
    print("Udaliaem ...")
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)


def zapis(data_, file_counter_):
    with open(f'{filepath_1}/newfile_{file_counter_}.csv', 'w+') as ff:
        ff.writelines(data_)


def devider():
    line_counter = 0
    file_counter = 0

    with open(filename) as f:
        header = next(f)
        data = [header]  # Поставили курсор на оглавление

        for i in f:
            if line_counter >= 498:
                line_counter = 0
                file_counter += 1
                zapis(data, file_counter)
                # print("Here we are")
                data = [header]
            data.append(i)
            line_counter += 1
        file_counter += 1
        if len(data) > 0:
            with open(f'{filepath_1}/newfile_{file_counter}.csv', 'w+', newline='') as ff:
                ff.writelines(
                    data)
    return file_counter


class Command(BaseCommand):

    def handle(self, *args, **options):
        import os

        if os.path.isdir(
                filepath_1):  ## Создали дериктори
            print('Есть директория: temp1')
        else:
            os.mkdir(filepath_1)
        devider()

        g = len(os.listdir(filepath_1))

        # gg = len(os.listdir(filepath_2))
