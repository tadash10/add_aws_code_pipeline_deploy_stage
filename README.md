# add_aws_code_pipeline_deploy_stage

AWS CodePipeline Setup Script

This script automates the setup of an AWS CodePipeline for your DevSecOps workflow, including source code integration from GitHub.
Prerequisites

Before using this script, ensure you have the following prerequisites:

    Python 3.6 or higher installed
    AWS CLI configured with necessary credentials and permissions

Installation

    Clone this repository to your local machine.

    bash

git clone https://github.com/yourusername/aws-codepipeline-setup.git
cd aws-codepipeline-setup

Create a Python virtual environment (optional but recommended).

bash

python3 -m venv venv
source venv/bin/activate

Install the required Python packages.

bash

    pip install -r requirements.txt

Usage
Step 1: Configuration

Edit the config.json file to configure your AWS CodePipeline and GitHub settings:

json

{
  "pipeline_name": "MyDevSecOpsPipeline",
  "github_owner": "your_github_username",
  "github_repo": "your_github_repository",
  "github_branch": "main",
  "github_oauth_token": "your_github_oauth_token",
  "aws_region": "your_aws_region"
}

Step 2: Running the Script

To create your AWS CodePipeline, run the following command:

bash

python create_code_pipeline.py

Step 3: Verify the Pipeline

After running the script, visit the AWS CodePipeline console to verify that your pipeline has been created successfully:

    Log in to the AWS Management Console.

    Navigate to the AWS CodePipeline service.

    You should see your pipeline (MyDevSecOpsPipeline) in the list of pipelines.

Step 4: Customize Further

You can further customize your pipeline by adding more stages and actions within the create_code_pipeline.py script.
Troubleshooting

    If you encounter issues with AWS credentials, ensure that your AWS CLI is configured correctly, or you can provide your AWS access key and secret key directly in config.json.
