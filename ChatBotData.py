#This file controls people in chat and their scores. As a starter built around 
# JSON files but will use SQLite in the future
import json

class TwitchUser():   
    def __init__(self,json_response):
        self.data = json.loads(json_response)               
    def __getId__(self):
        return self.data['_id']
    def __getName__(self):
        return self.data['display_name']
    
    
class UserScoreDatabase: 
    def __init__(self):
        self.admins = {}
        self.users = {}
    
    def __addUser__(self,_id,initialScore = 0):
        self.users[_id] =initialScore
        
    def __getScore__(self,_id):
        return self.users[_id].score
    
    def __addScore__(self,_id, qty):
        self.users[_id].score += qty
        
    def __setScoreTo__(self,_id,qty):
        self.users[_id].score = qty
    
    def __isAdmin__(self,_id):
        return self.users[_id] in admins.keys()
        
