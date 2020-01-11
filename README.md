# Python HTTP API client for Huawei Modems

This is a python library to interact with a Huawei modem over HTTP API.

The library has been tested on these devices:
* E5180
* E8372
* B315
* e3372h

Please let me know if you tested it successfully with other modems as well.

## Currently Supported

* webserver
   * get_session_token_info: gets a session token to use
* user
   * login: creates a new session on the HTTP API
* sms
   * get_sms: get information from boxes: inbox, outbox
   * send_sms: sends an SMS through device's modem
   * delete_sms: deletes an sms from one of their boxes
   * sms_count: get the sms count on each box
* ussd
   * status: get status of ussd. This will tell you if there are ussd messages available to read
   * send: sends a ussd message
   * get: retrieves a ussd message
* wlan:
    * get_connected_hosts: gets a list of connected devices
    * block_host: blocks the device from network
    * unblock_host: unblock device on network
    * get_blocked_hosts: gets a list of blocked devices
    * is_host_blocked: checks if device is blocked
* dialup:
    * connect_mobile: enables mobile (ie LTE / 4G / 3G / etc) network
    * disconnect_mobile: disables mobile network
    * get_mobile_status: checks the mobile connection status
* device:
    * reboot: reboots the modem

### Prerequisites

Only [`requests`](https://github.com/requests/requests) library (and its dependencies) is required.

This is `requirements.txt` content:

```
certifi==2018.11.29
chardet==3.0.4
idna>=2.6
requests>=2.0.0
urllib3>=1.22
```

### Installing

```bash
pip install huawei-modem-api-client-through-proxy
```

### Example
```python
import huaweisms.api.user
import huaweisms.api.wlan
import huaweisms.api.sms

ctx = huaweisms.api.user.quick_login("myusername", "mypassword")
print(ctx)
# output: <ApiCtx modem_host=192.168.8.1>

# sending sms
huaweisms.api.sms.send_sms(
    ctx,
    'phone-number',
    'this is the sms message'
)

# connected devices
device_list = huaweisms.api.wlan.get_connected_hosts(ctx)

```

Note: The default modem host is assumed to be `192.168.8.1`. If that is not the case for you, you can specify your modem ip as follows:

```python
import huaweisms.api.user
ctx = huaweisms.api.user.quick_login("myusername", "mypassword", modem_host='10.11.12.13')
print(ctx)

#output: <ApiCtx modem_host=10.11.12.13>
```

## Built With

* [requests](https://github.com/requests/requests) - Python HTTP Requests for Humans™

## Contributing

Send me a PM if you want to contribute. 

## Authors

* **Pablo Santa Cruz** - *Owner* - [pablo](https://github.com/pablo)
* **Mka Madlavana** - *Collaborator* - [dopstar](https://github.com/dopstar)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

