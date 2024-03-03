# # src/services/user_service.py
import json
import logging
import os
import time
import uuid

from ..dynamo_db.dynamodb import DynamoDB

class UserService:
    def __init__(self):
        self.db = DynamoDB()
        self.timestamp = str(time.time())

    def create_user(self, user_data):
        # Implement logic to create a user in the database
        try:
            
            item = {
                'id': user_data['email'],
                'name': user_data['name'],
                'checked': False,
                'createdAt': self.timestamp,
                'updatedAt': self.timestamp,
            }
            response =self.db.put_item(item)
            return str(response)
        except Exception as e:
            return str(e)

    def get_user(self, email):
        # Implement logic to retrieve a user from the database
        try:
            key={'id':email}
            response=self.db.get_item(key)
            return str(response)
        except Exception as e:
            return str(e)

    def update_user(self,email, user_data):
        # Implement logic to update a user in the database
        try:
            key={'id': email},
            updateExpression="set #name = :n",
            expressionAttributeNames={"#name": "name",},
            expressionAttributeValues={
                ":n": "John Doe",
            },
            response=self.db.update_item(key,updateExpression,expressionAttributeNames,expressionAttributeValues)
            return str(response)
        except Exception as e:
            return str(e)

    def delete_user(self, email):
        try:
            key={'id':email}
            response=self.db.delete_item(key)
            return str(response)
        except Exception as e:
            return str(e)


# import boto3

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('UserTable')

# def get_user(user_id):
#     # response = table.get_item(Key={'id': user_id})
#     # return response.get('Item')
#     response="get_user service called"
#     return response

# def create_user(user_data):
#     # response = table.put_item(Item=user_data)
#     response="create_user service called"
#     return response

# def update_user(user_id, user_data):
#     response="update service called"
#     # response = table.update_item(
#     #     Key={'id': user_id},
#     #     UpdateExpression='SET user_name = :user_name, age = :age, salary = :salary',
#     #     ExpressionAttributeValues={
#     #         ':user_name': user_data.get('user_name'),
#     #         ':age': user_data.get('age'),
#     #         ':salary': user_data.get('salary')
#     #     },
#     #     ReturnValues='ALL_NEW'
#     # )
#     return response

# def delete_user(user_id):
#     # response = table.delete_item(Key={'id': user_id})
#     response="delete_user service called"
#     return response