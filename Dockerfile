# Use official Python base image
FROM python:3.10-bullseye

# Set working directory
WORKDIR /app

# Copy requirements first (to leverage Docker caching)
COPY requirements.txt .

# Install packages, including torch+cpu from PyTorch index
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt \
    -f https://download.pytorch.org/whl/torch_stable.html

# Copy the rest of the app code
COPY ./app ./app

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

