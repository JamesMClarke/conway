class Square:
    def __init__(self,  is_alive):
        self.__is_alive = is_alive
    
    def get_is_alive(self):
        return self.__is_alive

    def kill(self):
        self.__is_alive = False

    def revive(self):
        self.__is_alive = True 