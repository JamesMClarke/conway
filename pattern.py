class Pattern():
    def __init__(self, name, pattern, type):
        self.__name = name
        self.__pattern = pattern
        self.__type = type

    def get_pattern(self):
        return self.__name, self.__pattern, self.__type

    def get_pattern_name(self):
        return self.__name
    
    def get_pattern_pattern(self):
        return self.__pattern
    
    def get_pattern_type(self):
        return self.__type