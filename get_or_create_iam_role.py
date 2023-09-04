import boto3
from botocore.exceptions import ClientError

def get_or_create_iam_role(session, iam_role_name):
    iam_client = session.client('iam')
    
    try:
        role = iam_client.get_role(RoleName=iam_role_name)
        return role['Role']['Arn']
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            iam_client.create_role(
                RoleName=iam_role_name,
                AssumeRolePolicyDocument='''{
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "codepipeline.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                }'''
            )
            role = iam_client.get_role(RoleName=iam_role_name)
            return role['Role']['Arn']
        else:
            raise
