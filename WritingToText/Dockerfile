# Use an official Python runtime based on Windows Server Core
FROM python:3.11-slim-buster

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set the secret key as an environment variable
ENV SECRET_KEY=django-insecure-fhhh_si5j_y*z^vx1%vnpkzlmgzkjzn3)n1v=nwx@hvxx^a=x-

# Copy project
COPY . /code/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]