# 4. Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import json
import csv


def new_users(csv_file: str, json_file: str) -> None:
    with (
        open(csv_file, mode='r', newline='', encoding='utf-8') as f_csv,
        open(json_file, mode='w', encoding='utf-8') as f_json
    ):
        csv_read = csv.reader(f_csv, dialect='excel')
        al_data = []
        for row in csv_read:
            user = {}
            user['id'] = f"{row[0]:0>10}"
            user['name'] = row[1].capitalize()
            user['level'] = row[2]
            user['hash'] = hash(f"{user['id']}{user['name']}")
            al_data.append(user)
            json.dump(al_data, f_json, indent=2)


def read_csv(csv_file: str) -> list[list[str]]:
    result = []
    with open(csv_file, 'r', encoding='utf-8') as f_in:
        for line in f_in.readlines():
            result.append(line.strip().split(';'))
    return result


def to_format(data: list[list[str]]) -> list[dict[str]]:
    data_lst = []
    for record in data:
        user_hash = hash(int(record[1])) + hash(record[2])
        data_lst.append(dict(user_hash=user_hash, user_id=f'{record[1]:0>10}',
                             user_name=record[2].capitalize(), access_level=record[0]))
    return data_lst


def write_json(data: list[dict[str, str]], json_file: str) -> None:
    with open(json_file, 'a', encoding='utf-8') as f_out:
        for line in data:
            f_out.write(str(line) + '\n')


def starter(file_in: str, file_out: str) -> None:
    write_json(to_format(read_csv(file_in)), file_out)


def main():
    file_in_name = 'index.csv'
    if __name == '__main__':
        main()