# notifciaton in mobile ntfy.sh website for notification un jegan

import requests

requests.post("https://ntfy.sh/pyclass_test",
    data="Backup successful 😀".encode(encoding='utf-8'))