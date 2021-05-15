from abc import ABC
import pickle


class DAO(ABC):
    def __init__(self, datasource=''):
        self.datasource = datasource #arquivo pkl onde os dados estão/serão serializados
        self.objectCache = {} #atributo de classe por onde os dados a serem serializados serão manipulados
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.objectCache, open(self.datasource, 'wb'))
        #salvando as informações de objectCache no arquivo pkl

    def __load(self):
        self.objectCache = pickle.load(open(self.datasource, 'rb'))
        #adicionando as informações que estavam no arquivo pkl para o atributo objectCache

    def add(self, id, valor_ranking):
        self.objectCache[id] = valor_ranking
        self.__dump()

    def get_all(self):
        return list(self.objectCache.items())