Use this as an example:

You need to set initialize to True for the first time to authenticate your account.
Then you can set it to false and use sendWhatsappMessage

use the international format for the phone number (starting with +)  without space.


if __name__ == '__main__':
    phone_number = '+336........' #International format
    message = "Test Message !"

    ws = WhatsappSender()
    ws.initialize(True) # use ws.initialize(False) after correct authentication
    res = ws.sendWhatsappMessage(phone_number, message)
    if res == 0:
        print(f'Message: "{message}"\nwas sent to: "{phone_number}"')
