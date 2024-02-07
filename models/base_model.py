from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
            
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
    def save(self):
        self.updated_at = datetime.today()
        
    def to_dict(self):
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
        
    def __str__(self):
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

