from pathlib import Path
from save_file_info import get_dirs_json, write_json, write_csv, write_pickle
if __name__ == '__main__':

    dict_json = get_dirs_json('C:\\Users\\Сергей\\PycharmProjects\\GeekBrains\\seminar_8')
    write_json('dir_info_json.json', dict_json)
    write_csv('dir_info_csv.csv', dict_json)
    write_pickle('dir_info_picle.pickle', dict_json)