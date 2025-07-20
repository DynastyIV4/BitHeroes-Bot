import json
import os
from dataclasses import asdict, fields
from enum import Enum


class BaseSettings:

    def __post_init__(self):
        self._load_settings()

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if hasattr(self, "_file_path") and self._file_path and key != "_file_path":
            self.save()

    def _load_settings(self):
        if not self._file_path or not os.path.exists(self._file_path):
            return

        try:
            with open(self._file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(self._file_path, "w") as f:
                json.dump({}, f)
                data = {}

        for f_ in fields(self):
            value = data.get(f_.name, getattr(self, f_.name))
            if isinstance(getattr(self, f_.name), Enum):
                enum_class = type(getattr(self, f_.name))
                setattr(self, f_.name, enum_class(value))
            else:
                setattr(self, f_.name, value)

    def save(self):
        if not self._file_path:
            raise ValueError("No _file_path set for settings class.")

        data = asdict(self)
        for key, value in data.items():
            if isinstance(value, Enum):
                data[key] = value.value

        data.pop("_file_path", None)
        with open(self._file_path, "w") as f:
            json.dump(data, f, indent=4)

    def set_and_save(self, key, value):
        setattr(self, key, value)
