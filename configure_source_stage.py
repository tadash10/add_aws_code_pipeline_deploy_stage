def configure_source_stage(github_owner, github_repo, github_branch, github_oauth_token):
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
    
    return source_stage
