#!c:\users\cosmin\desktop\faculta_2021-2022\sem1\se_labs\dot-splt\server\dotspltenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autobahn==21.11.1','console_scripts','xbrnetwork-ui'
__requires__ = 'autobahn==21.11.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autobahn==21.11.1', 'console_scripts', 'xbrnetwork-ui')()
    )
