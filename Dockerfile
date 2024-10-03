# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world (this is Flask's default port)
EXPOSE 5000

# Run the Python script (ensure the script is named properly)
CMD ["python", "app1.py"]
