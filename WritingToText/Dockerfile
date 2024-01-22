# Use an official Python runtime based on Windows Server Core
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Install Python
RUN powershell.exe -Command \
    $ErrorActionPreference = 'Stop'; \
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; \
    wget https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile c:\temp\python-installer.exe; \
    Start-Process c:\temp\python-installer.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait; \
    Remove-Item c:\temp\python-installer.exe

# Install pip
RUN python -m ensurepip --upgrade

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Set the secret key as an environment variable
ENV SECRET_KEY=django-insecure-fhhh_si5j_y*z^vx1%vnpkzlmgzkjzn3)n1v=nwx@hvxx^a=x-

# Copy project
COPY . /code/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]