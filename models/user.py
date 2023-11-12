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

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """Inintalization"""
        super().__init__(*args, **kwargs)