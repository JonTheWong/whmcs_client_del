# WHMCS DEL CLIENT
Script that used the API to delete a range of clients, has a feature for timeout.

## Config
create a file called .env add your keys and config

```
DEVMODE = 1

DEV_WHMCS_API_URI = 'https://jonthewong.com/dev/includes/api.php'
DEV_WHMCS_API_IDENT = 'AwJPRTmEVrBV_AwG7M82EeS9hBkwXHwP'
DEV_WHMCS_API_SECRET = 'AwJPRTmEVrBV_AwG7M82EeS9hBkwXHwP'

PROD_WHMCS_API_URI = 'https://jonthewong.com/prod/includes/api.php'
PROD_WHMCS_API_IDENT = 'AwJPRTmEVrBV_AwG7M82EeS9hBkwXHwP'
PROD_WHMCS_API_SECRET = 'AwJPRTmEVrBV_AwG7M82EeS9hBkwXHwP'
```

## Run

```
whmcs_del_client.py 30 100 3
```

Would delete users starting from 30 till it reaches the id of 100, and will pause for 3 seconds.


## Help

```
whmcs_del_client -h
```
