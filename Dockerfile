FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY models /app/models
COPY nltkdata /app/nltkdata

COPY requirements.txt .

# Install the specified packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy function code
COPY app.py .

# Expose any necessary ports (if your application requires it)
# EXPOSE 8080

# Set the CMD to your handler or main application script
CMD ["python", "app.py"]
