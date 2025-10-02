# Razorpay Webhook Listener
This project is designed to implement a minimal and secure webhook listener system that accepts mocked payment status updates from payment providers like Razorpay and PayPal. 

## Prerequisites
- Python
- Django framework
- SQLite (for local development)

## Steps to Set Up Locally: 
git clone https://github.com/Harshithaaaaareddy05/razorpay-webhook-listener.git

## Navigate to the project folder::
cd razorpay-webhook-listener

## if pip is not installed, install it by running the following command:
python get-pip.py
## After installation, verify that pip is installed correctly: 
pip --version

## Install Django
pip install django

## Database setup (sqlite)
python manage.py migrate

## run develpopment server :
python manage.py runserver
##### webhook listener will now be running at http://127.0.0.1:8000/. You can start testing the webhook listener here.


## Screenshots of the webhook listener in action for reference
<img width="562" height="227" alt="Invalid_signature_output" src="https://github.com/user-attachments/assets/906483b4-01e6-4ead-a283-63b381db5f49" />
<img width="745" height="398" alt="Valid_signature_output" src="https://github.com/user-attachments/assets/8b2d6e63-9023-4278-89e7-f512aa9233d9" />
<img width="575" height="293" alt="Get_endpoint_output" src="https://github.com/user-attachments/assets/4d7b4ca4-f72f-4162-9d72-bc2b24751bc7" />

