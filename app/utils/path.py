import os

class Path:
    def __init__(self, root: str, data: dict):
        self.root = root
        self.data = data
        self.entrada = data.get("entrada")
        self.saida = data.get("saida")
        self.backup = data.get("backup")
        
    def createDir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            
        return path

    def getEntrada(self):
        path = os.path.join(self.root, self.entrada)
        path = self.createDir(path)
        
        return path
    
    def getSaida(self):
        path = os.path.join(self.root, self.saida)
        path = self.createDir(path)
        
        return path
    
    def getBackup(self):
        path = os.path.join(self.root, self.entrada, self.backup)
        path = self.createDir(path)
        
        return path
        