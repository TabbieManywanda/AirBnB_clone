#!/usr/bin/python3
"""class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """User"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
