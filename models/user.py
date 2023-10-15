#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    def __init__(self):
        """initiation"""
        super().__init__()
        self.email = ""
        self.password = ""
        self.First_name = ""
        self.Last_name = ""
