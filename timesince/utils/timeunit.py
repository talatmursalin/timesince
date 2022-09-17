class TimeUnit:
    def __init__(self, value, unit_type, units_locale, value_converter=None):
        self.value = value
        self.unit_type = unit_type
        self.units_locale = units_locale
        self.value_converter = value_converter

    def __get_subscript(self):
        if self.value <= 1:
            return self.units_locale[self.unit_type][0]
        return self.units_locale[self.unit_type][1]

    def __repr__(self):
        local_subscrpt = self.__get_subscript()
        local_unit = str(self.value)
        if self.value_converter:
            local_unit = self.value_converter(self.value)
        return f"{local_unit} {local_subscrpt}"

    def __str__(self) -> str:
        return self.__repr__()

    def __int__(self):
        return self.value
    
    def converted_value(self):
        if self.value_converter:
            return self.value_converter(self.value)
        return self.value

    def default_repr(self):
        if self.unit <= 1:
            return f"{self.value} {self.units_locale[self.unit_type][0]}"
        return f"{self.value} {self.units_locale[self.unit_type][1]}"