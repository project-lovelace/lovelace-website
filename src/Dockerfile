FROM python:3.7

WORKDIR /usr/src/app

# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update &&\
    apt-get install -y --no-install-recommends postgresql-client netcat

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
