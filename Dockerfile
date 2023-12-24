# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project.wsgi:application"]
