FROM python:3.9-slim

# Set the working directory
WORKDIR /home/data

# Copy Python script and text files to the container
COPY script.py ./
COPY IF-1.txt ./
COPY AlwaysRememberUsThisWay-1.txt ./

# Ensure output directory exists
RUN mkdir -p /home/data/output && chmod -R 777 /home/data/output


# Set the command to run the script
CMD ["python", "/home/data/script.py"]

