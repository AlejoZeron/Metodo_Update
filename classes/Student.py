from classes.DbMongo import DbMongo


class Student:
    
    def __init__(self, Name, LastName, Telephone):
        self.name = Name
        self.LastName = LastName
        self.Telephone = Telephone

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()

    def update(self):
        client, db = DbMongo.connect()
        collection = db[self.LastName]
        collection.insert(self.__dict__)
        client.close()

        
    
    
        