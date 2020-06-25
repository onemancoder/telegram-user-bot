### Using Telethon to perform integration test

When building a [Telegram bot](https://core.telegram.org/bots/api), things can get complicated quickly and performing manual tests to ensure flows are implemented properly is time-consuming and error-prone.

Using [Telethon](https://github.com/LonamiWebs/Telethon) library to programmatically interact with a Bot _as though_ you are an actual user translates into increased confidence that the Bot is doing what it is supposed to do. 😊

#### Installing the required packages

```sh
$ pipenv install telethon # or pip3 depending on how you use Python
```

#### Getting Telegram App credentials

1. Go to https://my.telegram.org
1. Enter the mobile number that you use
1. Telegram will pop up a code for authentication, enter it into the web portal
1. You will see `App api_id` and `App api_hash`, this two will be required for the bot
1. **NOTE:** Do not share this information with anyone or check in to your source code, ever. 
1. Telegram does not allow revokation of App credentials so once leaked, you will not be able to prevent malicious parties from using them.

#### Authenticating for the first time

I chose to store the session as a `string` instead of file as I can place them in a `config.toml` file which helps when in comes to deploying in production.

The [User Guide](https://docs.telethon.dev/en/latest/concepts/sessions.html) talks about other methods so pick your own poison.

To authenticate for the first time:
```sh

$ cp config.sample.toml config.toml # Paste the api_id and api_hash credentials inside
$ pipenv run python3 first_time.py

Please enter your phone (or bot token): +123456789
Please enter the code you received: 123456
Please enter your password: 
Signed in successfully as Kenneth Lim

e0u10nxue90n09n9u10u9ne0uen0u2e1290eun0xu1eu290nex1092nuxe0ux102enux01u9enx0u2en0uxe091enux0912nue09xenu091u2ne09x1ue29unx02n0129uenx0u2190uex0912enux091unex019ue0n1u90en1092uenx019uen0x1ue09ue9e2
```

The long string printed out at the end will be an `authentication key`. You can now add it to `auth_string` inside `config.toml`


#### Useful Resources

1. https://gist.github.com/Bibo-Joshi/75f135edf1ca3530decf4c2ae06bd699
1. https://gist.github.com/jsmnbom/2e8044ca5cc55813a0e0380ad375b320