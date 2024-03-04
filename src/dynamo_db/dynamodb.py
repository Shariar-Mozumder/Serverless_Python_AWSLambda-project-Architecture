import boto3

class DynamoDB:
    def __init__(self, table_name='UserTable'):
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

    def update_item(self, key, update_fields):
        update_expression_parts = []
        expression_attribute_values = {}
        
         # Construct the UpdateExpression and ExpressionAttributeValues dynamically
        for i, (field_name, field_value) in enumerate(update_fields.items()):
            update_expression_parts.append(f"#{field_name} = :value{i}")
            expression_attribute_values[f":value{i}"] = field_value
        
        # Join the UpdateExpression parts into a single string
        update_expression = "SET " + ", ".join(update_expression_parts)

        # Execute the update_item operation with the constructed expression and values
        response = self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeNames={f"#{field_name}": field_name for field_name in update_fields.keys()},
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='UPDATED_NEW'
        )
        updated_item = response.get('Attributes')
        return updated_item

    def delete_item(self, key):
        response = self.table.delete_item(Key=key)
        return response
