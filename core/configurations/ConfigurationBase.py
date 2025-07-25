import json
import os
from abc import ABC
from dataclasses import fields
from enum import Enum


class ConfigurationBase(ABC):
    
    def __init__(self, file_path: str):
        self._file_path = file_path
        
        if os.path.exists(self._file_path):
            self.load()
    
    def load(self) -> None:
        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self._apply_loaded_data(data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load settings from {self._file_path}: {e}")
    
    def save(self) -> None:
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        
        data = self._serialize()
        
        try:
            with open(self._file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving settings to {self._file_path}: {e}")
    
    def _apply_loaded_data(self, data: dict) -> None:
        for field in fields(self):
            if field.name.startswith('_'):
                continue
                
            if field.name in data:
                value = data[field.name]
                current_value = getattr(self, field.name)
                
                if isinstance(current_value, Enum):
                    enum_class = type(current_value)
                    try:
                        value = enum_class(value)
                    except ValueError:
                        print(f"Warning: Invalid enum value {value} for {field.name}")
                        continue
                
                setattr(self, field.name, value)
    
    def _serialize(self) -> dict:
        data = {}
        
        for field in fields(self):
            if field.name.startswith('_'):
                continue
                
            value = getattr(self, field.name)
            
            if isinstance(value, Enum):
                value = value.value
            
            data[field.name] = value
        
        return data