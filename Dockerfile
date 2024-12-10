# Use an official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional, if needed for debugging or API)
EXPOSE 8080

# Run the bot
CMD ["python", "bot.py"]
