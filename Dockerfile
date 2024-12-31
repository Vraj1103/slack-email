# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Define environment variables (optional, can be set on Render as well)
# ENV SENDGRID_API_KEY=your_sendgrid_api_key
# ENV SENDGRID_PARSE_SECRET=your_sendgrid_parse_secret

# Command to run the FastAPI app with Uvicorn (as the ASGI server)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
