FROM python:3

ARG project_dir=/projects/
WORKDIR $project_dir

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install pytest pytest-flake8 pytest-cov
RUN pip install --no-cache-dir -r requirements.txt
