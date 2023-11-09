#!/usr/bin/python3
import json

class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        key ="{}.{}".format(self.__class__.__name__, obj.id)
        self.__objects[key] = obj
    def save(self):
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass