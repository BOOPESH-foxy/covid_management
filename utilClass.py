from sqlalchemy import MetaData
class DB:
    def __init__(self,session):
        self.Session = session()
        self.metadata = MetaData()