import boto3

class DynamoDB:
    def __init__(self, table_name='Usertable'):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(table_name)

    def put_item(self, item_data):
        response = self.table.put_item(Item=item_data)
        return response

    def get_item(self, key):
        response = self.table.get_item(Key=key)
        item = response.get('Item')
        return item

    def update_item(self, key, update_expression, expression_attribute_values):
        response = self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='UPDATED_NEW'
        )
        updated_item = response.get('Attributes')
        return updated_item

    def delete_item(self, key):
        response = self.table.delete_item(Key=key)
        return response
