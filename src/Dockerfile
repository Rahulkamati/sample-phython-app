# Use official Python Alpine image (small footprint)
FROM python:3.10-alpine

# Set working directory inside the container
WORKDIR /app

# Install build dependencies needed for some Python packages on Alpine
# (many wheels need gcc/musl-dev to build C extensions)
RUN apk add --no-cache gcc musl-dev linux-headers

# Copy only requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables (optional but common)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the app
CMD ["python", "app.py"]