import boto3
import os
from botocore.exceptions import ClientError

# AWS credentials and region configuration
aws_access_key = "your_access_key"
aws_secret_key = "your_secret_key"
aws_region = "your_aws_region"

# Create an AWS CodePipeline
def create_code_pipeline():
    client = boto3.client(
        'codepipeline',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )
    
    try:
        response = client.create_pipeline(
            pipeline={
                'name': 'MyDevSecOpsPipeline',
                'roleArn': 'arn:aws:iam::123456789012:role/CodePipeline-Role',
                # Configure source stage (e.g., GitHub, CodeCommit, etc.)
                'stages': [
                    {
                        'name': 'Source',
                        'actions': [
                            {
                                'name': 'SourceAction',
                                'actionTypeId': {
                                    'category': 'Source',
                                    'owner': 'ThirdParty',
                                    'provider': 'GitHub',
                                    'version': '1'
                                },
                                'configuration': {
                                    'Owner': 'your_github_username',
                                    'Repo': 'your_github_repository',
                                    'Branch': 'main',
                                    'OAuthToken': 'your_github_oauth_token'
                                }
                            }
                        ]
                    },
                    # Add more stages as needed (e.g., Build, Test, Deploy, etc.)
                ]
            }
        )
        print("Pipeline created successfully.")
    except ClientError as e:
        print("Error creating pipeline: ", e)

# Main function
if __name__ == "__main__":
    create_code_pipeline()
