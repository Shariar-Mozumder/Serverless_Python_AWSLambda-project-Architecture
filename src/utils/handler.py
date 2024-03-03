import json


# def hello(event, context):
#     body = {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "input": event
#     }

#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }

#     return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    # """
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }
    # """

# src/handler.py

# from src.views.user_view import create_user, get_user, update_user, delete_user
# from src.views.account_view import create_account, get_account, update_account, delete_account
# from src.views.authentication_view import authenticate_user
# from src.utils.responses import success_response,error_response

# def lambda_handler(event, context):
#     # Route requests to the appropriate view functions based on the request path
#     resource = event.get('resource', '')
#     http_method = event.get('httpMethod', '')
    
#     if resource.startswith('/users'):
#         if http_method == 'POST':
#             return create_user(event, context)
#         elif http_method == 'GET':
#             return get_user(event, context)
#         elif http_method == 'PUT':
#             return update_user(event, context)
#         elif http_method == 'DELETE':
#             return delete_user(event, context)
    # elif resource.startswith('/accounts'):
    #     if http_method == 'POST':
    #         return create_account(event, context)
    #     elif http_method == 'GET':
    #         return get_account(event, context)
    #     elif http_method == 'PUT':
    #         return update_account(event, context)
    #     elif http_method == 'DELETE':
    #         return delete_account(event, context)
    # elif resource.startswith('/authenticate'):
    #     if http_method == 'POST':
    #         return authenticate_user(event, context)
    
    # Return error response for unsupported routes
    # return error_response(404, 'Not Found')

# from fastapi import FastAPI
# from fastapi.middleware.wsgi import WSGIMiddleware
# from views.user_view import app as user_app
# from fastapi_lambda.wsgi import handle_request

# app = FastAPI()

# # Mount user view app
# app.mount("/user", user_app)

# # Wrap the FastAPI app with WSGI middleware for AWS Lambda
# app = WSGIMiddleware(app)

# # Define Lambda handler function
# def lambda_handler(event, context):
#     # Pass the event to the WSGI handler
#     return handle_request(app, event, context)

from src.views.user_view import lambda_handler_view

def lambda_handler(event, context):
    response= lambda_handler_view(event, context)
    return {
    "statusCode": 200,
    "body": "response:  "+str(response)
    }
