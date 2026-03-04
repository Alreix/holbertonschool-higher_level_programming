#!/usr/bin/python3
"""
Define the State model mapped to the 'states' table.

This module provides:
- Base: the declarative base class
- State: the ORM model for the states table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State model representing a row in the 'states' table."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)