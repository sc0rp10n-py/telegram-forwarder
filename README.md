# Telegram Forwarder

Supports
- user accounts
- private channels
- public channels

## Installation

```bash
git clone <url>
cd telegram-forwarder
# create env
python3 -m venv env
# activate env
source env/bin/activate
# install requirements
pip install -r requirements.txt
```

## Usage

First got to `.env` file and add your credentials.

```js
API_ID = <api-id>
API_HASH = <api-hash>
FROM_CHANNEL_ID = <enter-from-channel-id>
TO_CHANNEL_ID = <enter-to-channel-id>
PHONE_NUMBER = <phone-number>
SESSION_NAME = <session-name> # can just enter "session"
```

Then run the script.

```bash
# activate env
source env/bin/activate
# run
python3 main.py
```