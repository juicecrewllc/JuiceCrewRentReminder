import os
import datetime
import logging
from azure.communication.sms import SmsClient
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    # Get connection string from environment
    connection_string = os.environ["COMMUNICATION_SERVICES_CONNECTION_STRING"]

    sms_client = SmsClient.from_connection_string(connection_string)

    # Replace with tenant phone numbers
    phone_numbers = ["+2144296720", ""]

    for number in phone_numbers:
        sms_client.send(
            from_="+18332542843",  # Your ACS phone number
            to=number,
            message="Reminder: Rent is due tomorrow. Please make your payment."
        )

    logging.info(f"Python timer trigger function executed at {utc_timestamp}")
