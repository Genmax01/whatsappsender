Use this as an example:

You need to set initialize to True for the first time to authenticate your account.
Then you can set it to false and use sendWhatsappMessage

    def initialize(self, firstRun=False, pathToUserData='', userAgent='', pathToBrowser=''):
        """

        :param firstRun: bool Set to True the first time to log in to your whatsapp account
        :param pathToUserData: string You can specify your user data browser folder (Profile)
        :param userAgent: string You can use a specific user agent
        :param pathToBrowser string You can specify where to find you preferred browser
        :return:
        """

    

use the international format for the phone number (starting with +)  without space.

        def sendWhatsappMessage(self, phone_number, message):
        """

        :param phone_number: in international format +XXXXXXXXXXX
        :param message:
        :return:
        """


Example code to use it correctly:

    from whatsappsender import *


    phone_number = '+336........' #International format
    message = "Test Message !"

    ws = WhatsappSender()
    ws.initialize(True) # use ws.initialize(False) after correct authentication
    res = ws.sendWhatsappMessage(phone_number, message)
    if res == 0:
        print(f'Message: "{message}"\nwas sent to: "{phone_number}"')
