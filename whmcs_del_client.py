import requests
import time
import argparse
from decouple import config


# Create .env file with your settings
if config('DEVMODE') == str(1):
    API_URI = config('DEV_WHMCS_API_URI')
    API_IDENT = config('DEV_WHMCS_API_IDENT')
    API_SECRET = config('DEV_WHMCS_API_SECRET')
else:
    API_URI = config('PROD_WHMCS_API_URI')
    API_IDENT = config('PROD_WHMCS_API_IDENT')
    API_SECRET = config('PROD_WHMCS_API_SECRET')


def delwhmcsuser():
    parser = argparse.ArgumentParser(description='Enter a RANGE of userID\'s to perminantly delete, example; 0 100 will delete userID 0,1,2,3...20...50...100 one by one untill it reaches the end value.')
    parser.add_argument('start', metavar='N', type=int, help='The start of the userID range value')
    parser.add_argument('stop', metavar='N', type=int, help='The stop value of the userID')
    parser.add_argument('sleep', metavar='N', type=int, help='The amount of time to sleep in seconds between requests')
    args = parser.parse_args()
    # print(args)

    for userID in range(args.start, args.stop + 1):
        params = {'identifier': API_IDENT, 'secret': API_SECRET, 'responsetype': 'JSON', 'action': 'DeleteClient', 'clientid': userID, 'deleteusers': 'false', 'deletetransactions': 'false'}

        res = requests.post(API_URI, data=params, verify=True, timeout=120)
        logtime = time.strftime('%c')

        if res.status_code in range(400, 504):
            print(logtime, '>> QUIT LOOP >>', res.status_code, '<<')
            exit()
        else:
            print(logtime, res.text, '\n sleep for >>', args.sleep, '<< seconds')
            time.sleep(args.sleep)


delwhmcsuser()
