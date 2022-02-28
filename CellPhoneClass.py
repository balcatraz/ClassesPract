class cellphone:

    def __init__(self, mnf,mdl,rpr):
        self.__manufact = mnf
        self.__model = mdl
        self.__retailPrice = rpr

    def set_manufact(self, mnf):
        self.__manufact = mnf 

    def set_model(self, mdl):
        self.__model = mdl

    def set_retail_price(self, rpr):
        self.__retailPrice = rpr

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retailPrice
