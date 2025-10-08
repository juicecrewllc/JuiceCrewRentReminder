import logging
import os
from azure.communication.sms import SmsClient
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    logging.info("Rent reminder function triggered.")

    connection_string = os.environ.get("ACS_CONNECTION_STRING")
    if not connection_string:
        logging.error("ACS connection string not found.")
        return

    sms_client = SmsClient.from_connection_string(connection_string)

    try:
        response = sms_client.send(
            from_="+18666576701",
            to=["+12144296720"],
            message="REMINDER: Your rent payment is coming up TOMORROW 11/1/2025. Zelle payments are preferred (recipient: 2144296720) or a cashier/bank check made out to Emeka Eni will also be valid. Thank you! Emeka Eni"
        )

        for r in response:
            logging.info(f"Message ID: {r.message_id}, To: {r.to}, Success: {r.successful}")

    except Exception as e:
        logging.error(f"Error sending SMS: {e}")
