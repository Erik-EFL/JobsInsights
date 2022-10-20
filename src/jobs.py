from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        read_file = csv.reader(file)
        read_list = list(read_file)
    return read_list
