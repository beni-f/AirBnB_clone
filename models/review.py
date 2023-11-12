#!/usr/bin/python3
"""
Review Module
"""
from models.base_model import BaseModel
class Review(BaseModel):
    """Review Class"""
    def __init__(self):
        """Initialization"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""