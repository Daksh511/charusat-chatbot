# Use the official Python image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first (helps with caching layers)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory into the container
COPY backend /app/backend

# Expose the port (Ensure it matches the one used in your app.py)
EXPOSE 8000

# Run the application
CMD ["python", "/app/backend/app.py"]
