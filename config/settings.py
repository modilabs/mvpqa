COMMCARE_URL = u'https://www.commcarehq.org'
COMMCARE_USERNAME = u''
COMMCARE_PASSWORD = u''
CUSTOM_REPORTS = {
    'mvp-ruhiira': {
        'pregnancy-visit': '5b465124990a0e7c216b707109eb2cea',
        'household-visit': 'b1817d5823cce017ff35fdfaaf4b2f40',
        'child-visit': '91b622122dcf8f5807f62793dd5c6691'
    },
    'mvp-sauri': {
        'pregnancy-visit': '0481c2222ebfdb322b3e8115732c7507',
        'household-visit': '5d63706d5d62517a638926f2c59be20d',
        'child-visit': '51d3d33f94c4f7654e81ac443a59344d'
    }
}

FDURL = 'http://openrosa.org/formdesigner/'
FORM_XMLNS = {
    'mvp-ruhiira': {
        'child-close': FDURL + 'AC164B28-AECA-45C9-B7F6-E0668D5AF84B',
        'pregnancy-outcome': FDURL + '01EB3014-71CE-4EBE-AE34-647EF70A55DE',
        'death': FDURL + 'b3af1fddeb661ee045fef1e764995440ea8f057f',
    },
    'mvp-sauri': {
        'child-close': FDURL + 'AC164B28-AECA-45C9-B7F6-E0668D5AF84B',
        'pregnancy-outcome': FDURL + '01EB3014-71CE-4EBE-AE34-647EF70A55DE',
        'death': FDURL + 'b3af1fddeb661ee045fef1e764995440ea8f057f',
    }
}

try:
    from .local_settings import *
except:
    pass
