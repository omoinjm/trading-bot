# Use an official Python runtime as a parent image
FROM python:3.8 AS base

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the "src" directory into the container at /app
COPY ./ /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set up environment variables using build arguments
ARG PYTHON_ENV
ARG API_ENDPOINT
ARG TELEGRAM_TOKEN

ENV PYTHON_ENV=${PYTHON_ENV}
ENV API_ENDPOINT=${API_ENDPOINT}
ENV TELEGRAM_TOKEN=${TELEGRAM_TOKEN}

# Run the Python application (assuming app.py is your entry point)
CMD ["python", "app.py"]

