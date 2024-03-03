# # src/services/user_service.py

from ..dynamo_db.dynamodb import DynamoDB

class UserService:
    def __init__(self):
        self.db = DynamoDB()

    def create_user(self, user_data):
        # Implement logic to create a user in the database
        response =self.db.put_item(user_data)
        return response

    def get_user(self, user_id):
        # Implement logic to retrieve a user from the database
        response="get_user service called"
        return response

    def update_user(self, user_id, user_data):
        # Implement logic to update a user in the database
        response="Update User service called"
        return response

    def delete_user(self, user_id):
        response="get_user service called"
        return response


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