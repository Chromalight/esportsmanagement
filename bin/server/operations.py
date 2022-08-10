from pymongo import MongoClient
import hashlib
import uuid

client = MongoClient('localhost',27017) # Check the docs of MongoDB if you need information about self hosting your Mongo database.
userdb = client.userdata
basedata = userdb.basedata

if __name__ == '__main__':
    pass # Reserved for future usage.
else:

    def hashText(text):
        nonhex_pwd = hashlib.new('sha3_512', text.encode())
        return nonhex_pwd.hexdigest()

    def emailUsed(email):
        exists = basedata.find_one({'email': email})
        return bool(exists)


    def createUser(email, nickname, password, isManager: bool):
    
        if len(password) >= 10 and emailUsed(email):
        
            hashed_pwd = hashText(password)
            data =  {'_id': str(uuid.uuid1(node=49410872532555)), 'email': email, 'nickname': nickname, 'password': hashed_pwd, 'isManager': isManager}
            basedata.insert_one(data)
            # Email verification will be added in the future (Before production.)
        else:
            return 'The password should be at least 10 characters long.'


    def loginUser(email, password):

        data = {'email': email, 'password': hashText(password)} # Creating the list that will be used for the query.
        user = basedata.find_one(data)
        if bool(user):
            # Session system will be implemented when required.
            return 1

        else:
            return 0

