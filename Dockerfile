# Use an official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 8080

# Run the app
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

