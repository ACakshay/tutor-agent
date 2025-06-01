# Use official Python image
FROM python:3.11-slim

RUN pip install uv

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN uv pip install --system -r requirements.txt

# Copy application code
COPY . .

# Expose ASGI port
EXPOSE 8000

# Command to run ASGI app (replace 'app:app' with your ASGI app module)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]