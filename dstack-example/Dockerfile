# Use a slim Python base image for minimal footprint
FROM python:3.10-slim

# Install system dependencies (if any needed beyond Python)
RUN apt-get update \
 && apt-get install --no-install-recommends -y \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Create application directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI server code
COPY attestation_server.py .

# Expose the HTTP port
EXPOSE 5000

# Run with Uvicorn
CMD ["uvicorn", "attestation_server:app", "--host", "0.0.0.0", "--port", "5000"]
