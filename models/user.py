#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel
from models import storage

class User(BaseModel):
    """
    User class
    """
    def __init__(self):
        """Inintalization"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""