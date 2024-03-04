import json

def success_response(status_code, data):
    """
    Generate a success response with the given status code and data.

    Args:
        status_code (int): The HTTP status code.
        data (dict): The response data.

    Returns:
        dict: The success response.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps(data)
    }

def error_response(status_code, error_message):
    """
    Generate an error response with the given status code and error message.

    Args:
        status_code (int): The HTTP status code.
        error_message (str): The error message.

    Returns:
        dict: The error response.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps({'error': error_message})
    }
