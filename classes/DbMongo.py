import os
import pymongo

class DbMongo:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        print("Objeto creado")
    
    
    @staticmethod
    def getDB():
        user = os.envioron['NinrodZeron']
        password = os.environ['POO01']
        cluster = os.environ['cluster0.vra2pop.mongodb.net']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )
 
        client = pymongo.MongoClient(uri)
        db = client['unah']

        return client, db