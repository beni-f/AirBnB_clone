#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage
class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return str("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
         obj_dict = self.__dict__
         obj_dict['__class__'] = self.__class__.__name__
         obj_dict['created_at'] = self.created_at.isoformat()
         obj_dict['created_at'] = self.updated_at.isoformat()
         return obj_dict
    
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)