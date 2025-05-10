FROM python:3.11-slim

WORKDIR /app

# Install OS dependencies if needed (optional)
RUN apt-get update && apt-get install -y build-essential

# Create virtualenv
RUN python -m venv /opt/venv

# Set path
ENV PATH="/opt/venv/bin:$PATH"

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY . .

# Start app
CMD ["gunicorn", "app:app"]

