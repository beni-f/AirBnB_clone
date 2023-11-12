#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel
class City(BaseModel):
    """City Class"""
    def __init__(self):
        """Initialization"""
        self.state_id = ""
        self.name = ""