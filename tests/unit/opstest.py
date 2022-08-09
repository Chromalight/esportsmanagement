import unittest

from esportsmanagement.bin.server import operations


class TestOperations(unittest.TestCase):
    def testCreate(self):
        userData = {'email':"testmail@testserver.org",'nickname': "testnick", 'password': "testpassword123", 'isManager': True}
        operations.basedata.insert_one(userData)
        success = operations.basedata.find_one(userData)
        
        message = 'User creation/query test failed.'
        operations.basedata.delete_one(userData)
        self.assertTrue(bool(success), message)
        
    def testUpdate(self):
        testUser = {'email':'testmail@testserver.org', 'nickname': 'testnick', 'password': 'testpassword123', 'isManager': True}
        operations.basedata.insert_one(testUser)
        operations.basedata.update_one(testUser, {'$set': {'isManager': False}})
        testUser['isManager'] = False
        success = operations.basedata.find_one(testUser)
        message = 'User update test failed.'
        operations.basedata.delete_one(testUser)
        self.assertTrue(bool(success), message)

if __name__ == "__main__":
    unittest.main()
