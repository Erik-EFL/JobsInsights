from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as file:
        read_file = csv.DictReader(file)
        read_list = list(read_file)
    return read_list
