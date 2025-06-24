#WhatsApp Message Automation

from twilio.rest import Client
from datetime import datetime
import time

# Step 2: Twilio credentials 
account_sid = 'AC17069b52706d116511c11f017e56a363'
auth_token = '215e46d957f85d8e0d343b6d6a2e5975'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred:', str(e))

name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +91XXXXXXXXXX): ')
message_body = input(f'Enter the message you want to send to {name}: ')

#calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')  
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')  

try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()

    # Calculate delay
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print('The specified time is in the past. Please enter a future date and time.')
    else:
        print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
        time.sleep(delay_seconds)
        send_whatsapp_message(recipient_number, message_body)

except ValueError:
    print('Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM (24-hour) for time.')
