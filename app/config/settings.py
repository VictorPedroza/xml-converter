import os
import json
from app.utils.path import Path

class Settings:
    def __init__(self, file: str):
        self.file = file
        self.root = os.path.dirname(os.path.abspath(self.file))
        json_path = os.path.join(self.root, "config", "settings.json")

        with open(json_path, "r", encoding="utf-8") as arq:
            self.data = json.load(arq)
            
        path = Path(self.root, self.data)
        
        