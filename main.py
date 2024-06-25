import os
from datetime import datetime

def create_build_info_file(filename='BUILDINFO'):
    # Gather build information from GitLab CI/CD environment variables
    version = os.getenv('CI_JOB_NAME', '1.0.0')  # Replace '1.0.0' with a default or actual logic if needed
    build_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_hash = os.getenv('CI_COMMIT_SHA', 'unknown')
    branch_name = os.getenv('CI_COMMIT_REF_NAME', 'unknown')
    build_environment = os.getenv('CI_ENVIRONMENT_NAME', 'development')
    pipeline_id = os.getenv('CI_PIPELINE_ID', 'unknown')
    job_id = os.getenv('CI_JOB_ID', 'unknown')

    # Create the content of the BUILDINFO file
    build_info_content = f"""Version: {version}
Build Time: {build_time}
Commit Hash: {commit_hash}
Branch Name: {branch_name}
Build Environment: {build_environment}
Pipeline ID: {pipeline_id}
Job ID: {job_id}
"""

    # Write to the BUILDINFO file
    with open(filename, 'w') as file:
        file.write(build_info_content)

    print(f"{filename} file created successfully.")

# Run the function to create the BUILDINFO file
if __name__ == "__main__":
    create_build_info_file()
