FROM python:3.11-slim

WORKDIR /app

# Install Telethon directly (no requirements.txt needed)
RUN pip install --no-cache-dir telethon

# Copy your Python script into the container
COPY . .

# Run the bot when the container starts
CMD ["python", "main.py"]

