import boto3
from botocore.exceptions import ClientError

# Configuration variables
pipeline_name = 'MyDevSecOpsPipeline'
github_owner = 'your_github_username'
github_repo = 'your_github_repository'
github_branch = 'main'
github_oauth_token = 'your_github_oauth_token'
aws_region = 'your_aws_region'
iam_role_name = 'CodePipeline-Role'

# Create an AWS CodePipeline
def create_code_pipeline():
    try:
        # Initialize an AWS session with the specified region
        session = boto3.Session(region_name=aws_region)
        
        # Create an AWS CodePipeline client using the session
        codepipeline_client = session.client('codepipeline')

        # Define the IAM role ARN for the pipeline
        iam_role_arn = get_or_create_iam_role(session)

        # Configure the source stage (GitHub in this example)
        source_stage = {
            'name': 'Source',
            'actions': [
                {
                    'name': 'SourceAction',
                    'actionTypeId': {
                        'category': 'Source',
                        'owner': 'AWS',
                        'provider': 'GitHub',
                        'version': '1'
                    },
                    'configuration': {
                        'Owner': github_owner,
                        'Repo': github_repo,
                        'Branch': github_branch,
                        'OAuthToken': github_oauth_token
                    }
                }
            ]
        }
        
        # Define more stages and actions as needed
        
        # Create the pipeline
        response = codepipeline_client.create_pipeline(
            pipeline={
                'name': pipeline_name,
                'roleArn': iam_role_arn,
                'stages': [source_stage]
                # Add more stages here
            }
        )
        
        print("Pipeline created successfully.")
    except ClientError as e:
        print("Error creating pipeline: ", e)

# Create or retrieve the IAM role for the pipeline
def get_or_create_iam_role(session):
    iam_client = session.client('iam')
    
    try:
        role = iam_client.get_role(RoleName=iam_role_name)
        return role['Role']['Arn']
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            # The role does not exist, create it
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
            # Attach necessary policies to the role as needed
            # iam_client.attach_role_policy(RoleName=iam_role_name, PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')
            
            role = iam_client.get_role(RoleName=iam_role_name)
            return role['Role']['Arn']
        else:
            raise

# Main function
if __name__ == "__main__":
    create_code_pipeline()
