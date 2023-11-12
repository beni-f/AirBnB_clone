#!/usr/bin/python3
"""
Amenity Module
"""
from models.base_model import BaseModel
class Amenity(BaseModel):
    """Amenity Class"""
    def __init__(self):
        """Initialization"""
        self.name = ""