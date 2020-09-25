import os
from shutil import copyfile

source_path = '/Users/vl2drob/Music/Звёзды зарубежного рока'  # Source music folder
dest_path = '/Users/vl2drob/Music/Rock sorted'  # Folder for sorted music


def dir_crawler(path):
    _track_sorter(path)
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            dir_crawler(path + '/' + i)


def _track_sorter(path):
    for item in os.listdir(path):
        if item.endswith(".mp3"):
            artist_name = item.split('-')[1]
            if artist_name.endswith(' '):
                artist_name = artist_name[:-1:]
            dir = dest_path + '/' + artist_name
            if not os.path.exists(dir):
                os.makedirs(dir)
            copyfile(path + '/' + item, dir + '/' + item)


def main():
    dir_crawler(source_path)


if __name__ == "__main__":
    main()
