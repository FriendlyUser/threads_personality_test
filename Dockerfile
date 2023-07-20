# Use the official Python image as the base image
FROM python:3.10-slim-buster 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory 
COPY ./ /app

# Expose port 80 for the API
EXPOSE 80

# Set environment variables (if any)
# ENV ...

# Run the API when the container launches 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]