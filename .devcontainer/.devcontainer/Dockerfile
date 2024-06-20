FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install any additional tools or dependencies here
RUN pip install --upgrade pip

# Install dependencies from requirements.txt if available
COPY requirements.txt /tmp/pip-tmp/
RUN pip install -r /tmp/pip-tmp/requirements.txt
RUN rm -rf /tmp/pip-tmp
