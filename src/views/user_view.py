# # src/views/user_view.py

# from src.services.user_service import UserService
# from src.utils.responses import success_response, error_response

# user_service = UserService()

# def create_user(event, context):
#     # Implement logic to create a user
#     pass

# def get_user(event, context):
#     # Implement logic to retrieve a user
#     pass

# def update_user(event, context):
#     # Implement logic to update a user
#     pass

# def delete_user(event, context):
#     # Implement logic to delete a user
#     pass

# from fastapi import FastAPI, HTTPException
# from services.user_service import get_user, create_user, update_user, delete_user

# app = FastAPI()

# @app.get("/users/{user_id}")
# def read_user(user_id: str):
#     user = get_user(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @app.post("/users/")
# def create_user_api(user_data: dict):
#     response = create_user(user_data)
#     return response

# @app.put("/users/{user_id}")
# def update_user_api(user_id: str, user_data: dict):
#     user = get_user(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     response = update_user(user_id, user_data)
#     return response

# @app.delete("/users/{user_id}")
# def delete_user_api(user_id: str):
#     user = get_user(user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     response = delete_user(user_id)
#     return response

import json
# from src.services.user_service import get_user, create_user, update_user, delete_user
from src.services.user_service import UserService

def lambda_handler_view(event, context):
    http_method = event['httpMethod']
    path = event['path']
    user_service=UserService()
    # return {"event":str(event)}
    
    # if http_method == 'GET':
    #     if path == '/users/{user_id}':
    #         user_id = event['pathParameters']['user_id']
    #         user = get_user(user_id)
    #         if user:
    #             return {
    #                 'statusCode': 200,
    #                 'body': json.dumps(user)
    #             }
    #         else:
    #             return {
    #                 'statusCode': 404,
    #                 'body': json.dumps({'error': 'User not found'})
    #             }
    
    if http_method == 'POST':
        if path == '/getUser':
            user_data = json.loads(event['body'])
            email=user_data.get('email')
            response = user_service.get_user(email)
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }
        
        if path == '/insertUser':
            user_data = json.loads(event['body'])
            # user_id=user_data.get('user_id')
            response = user_service.create_user(user_data)
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }
        
        if path == '/updateUser':
            user_data = json.loads(event['body'])
            email=user_data.get('email')
            response = user_service.update_user(email,user_data)
            return {
                'statusCode': 200,
                'body': response #json.dumps(response)
            }
        
        if path == '/deleteUser':
            user_data = json.loads(event['body'])
            email=user_data.get('email')
            response = user_service.delete_user(email)
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }
    
    # elif http_method == 'PUT':
    #     if path == '/users/{user_id}':
    #         user_id = event['pathParameters']['user_id']
    #         user_data = json.loads(event['body'])
    #         response = update_user(user_id, user_data)
    #         return {
    #             'statusCode': 200,
    #             'body': json.dumps(response)
    #         }
    
    # elif http_method == 'DELETE':
    #     if path == '/users/{user_id}':
    #         user_id = event['pathParameters']['user_id']
    #         response = delete_user(user_id)
    #         return {
    #             'statusCode': 200,
    #             'body': json.dumps(response)
    #         }
    
    return {
        'statusCode': 400,
        'body': json.dumps({'error': 'Invalid request'})
    }


