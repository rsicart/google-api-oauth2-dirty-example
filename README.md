# Testing Google APIs using Oauth2

It's just some testing stuff, nothing more.
So use it carefully.

To test it you can use a virtualenv...

```
me@localhost~$ mkdir -p ~/virtualenvs
me@localhost~$ virtualenv --python=/usr/bin/python3 ~/virtualenvs/oauth2
me@localhost~$ source ~/virtualenvs/oauth2/bin/activate
me@localhost~$ pip install --upgrade google-api-python-client
me@localhost~$ pip install pyopenssl
```
After that, create all Google developer console project setup settings.

Fill json sample with it, or export a p12 credentials file.

Launch the script `drive.py`
