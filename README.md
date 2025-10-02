# Razorpay Webhook Listener
This project is designed to implement a minimal and secure webhook listener system that accepts mocked payment status updates from payment providers like Razorpay and PayPal. 

## Prerequisites
- Python
- Django framework
- SQLite (for local development)

### Steps to Set Up Locally: 
git clone https://github.com/Harshithaaaaareddy05/razorpay-webhook-listener.git

#### Navigate to the project folder::
cd razorpay-webhook-listener

##### if pip is not installed, install it by running the following command:
python get-pip.py
### After installation, verify that pip is installed correctly: 
pip --version

# Install Django
pip install django

# Database setup (sqlite) 
python manage.py makemigrations
python manage.py migrate

## run develpopment server :
python manage.py runserver
##### webhook listener will now be running at http://127.0.0.1:8000/. You can start testing the webhook listener here.
