import boto3
client = boto3.client('ssm', region_name='us-east-1')

def list_automation(name):
    response = client.list_documents(
        # posso adicionar tags
        DocumentFilterList=[
            {
                'key': 'Name',
                'value': f'{name}',
            },
        ]
    )
    return response['DocumentIdentifiers'][0]


def execution_automation(name):
    response = client.start_automation_execution(
        DocumentName=f'{name}'
    )
    return {'AutomationExecutionId': response['AutomationExecutionId']}