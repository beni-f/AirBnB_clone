#!/usr/bin/python3
"""
base_model module
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
        BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """String Representation of the class"""
        return str("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        """update the public instance attribute
            update_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containig all keys/values of __dict__ of the instance"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = dict_obj['created_at'].isoformat()
        dict_obj['updated_at'] = dict_obj['updated_at'].isoformat()
        return dict_obj
