PASSWORDS = {
    'email': '1234emaillekijen/emial-password',
    'blog': 'blogpasswordfor-testing-blog',
    'mac': 'macpasseord//////===-09yes-mac'
}

import sys
if len(sys.argv) < 2:
    print('Usage: Python simple_password_manager.py [account] - copy password.')
    sys.exit()

account = sys.argv[1]

import pyperclip

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied in clipboard.')
else:
    print('No this account ' + account)