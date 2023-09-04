import boto3
from botocore.exceptions import ClientError

def create_code_pipeline(pipeline_name, github_owner, github_repo, github_branch, github_oauth_token, aws_region):
    try:
        session = boto3.Session(region_name=aws_region)
        codepipeline_client = session.client('codepipeline')
        iam_role_arn = get_or_create_iam_role(session, 'CodePipeline-Role')
        
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
        
        response = codepipeline_client.create_pipeline(
            pipeline={
                'name': pipeline_name,
                'roleArn': iam_role_arn,
                'stages': [source_stage]
            }
        )
        
        print("Pipeline created successfully.")
    except ClientError as e:
        print("Error creating pipeline: ", e)
