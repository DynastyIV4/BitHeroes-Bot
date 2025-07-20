class PointerAddress:
    def __init__(self, module: str, base: int, offsets: list[int], value_type: str):
        self.base = base
        self.module = module
        self.offsets = offsets
        self.value_type = value_type

    @property
    def value_type(self):
        return self._value_type

    @value_type.setter
    def value_type(self, value: str):
        if value not in ['int', 'bool']:
            raise ValueError("This value type is not supported.")
        self._value_type = value

    def __repr__(self):
        return f"<MemoryAddress base={hex(self.base)} module={self.module} value_type={self.value_type}>"
