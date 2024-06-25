import os

from datetime import datetime


def create_build_info_file(filename='BUILDINFO'):
    # Gather build information from GitLab CI/CD environment variables
    name = os.getenv('CI_PROJECT_NAME', 'unknown')
    version = os.getenv('CI_JOB_NAME', '0.0.0')
    time = datetime.now().strftime('%a %d-%m-%Y %H:%M:%S')
    environment = os.getenv('CI_ENVIRONMENT_NAME', 'unknown')
    branch = os.getenv('CI_COMMIT_BRANCH', 'unknown')
    username = os.getenv('GITLAB_USER_LOGIN', 'unknown')

    # Create the content of the BUILDINFO file
    build_info_content = f"""Name: {name}
Version: {version}
Build Time: {time}
Environment: {environment}
Branch Name: {branch}
Creator: {username}"""

    # Write to the BUILDINFO file
    with open(filename, 'w') as file:
        file.write(build_info_content)

    print(f"{filename} file created successfully.")


# Run the function to create the BUILDINFO file
if __name__ == "__main__":
    create_build_info_file()
