# coding=utf-8
from __future__ import absolute_import

import importlib

__thg_module__ = [
    'thg_server',
    'thg_version',
    'thg_shells',
    'thg_docs',
    'thg_auxiliares',
    'thg_anti_forensic',
    'thg_crypto',
    'thg_drone',
    'thg_keylogger',
    'thg_recon',
    'thg_voip',
    'thg_automation',
    'thg_cryptography',
    'thg_exploitation',
    'thg_malware',
    'thg_reversing',
    'thg_windows',
    'thg_automobile',
    'thg_database',
    'thg_fingerprint',
    'thg_misc',
    'thg_sniffer',
    'thg_wireless',
    'thg_auxiliares',
    'thg_debugger',
    'thg_firmware',
    'thg_mobile',
    'thg_social',
    'thg_backdoor',
    'thg_decompiler',
    'thg_forensic',
    'thg_networking',
    'thg_spoff',
    'thg_binary',
    'thg_defensensive',
    'thg_gpu',
    'thg_os',
    'thg_nfc',
    'thg_nfc',
    'thg_spoof',
    'thg_version',
    'thg_bluetooth',
    'thg_defensive',
    'thg_hardware',
    'thg_packer',
    'thg_stego',
    'thg_code_audit',
    'thg_disassembler',
    'thg_honeypot',
    'thg_proxy',
    'thg_tunnel',
    'thg_cracker',
    'thg_dos',
    'thg_ids',
    'thg_radio',
    'thg_unpacker',
    'thg_auxiliares'
]

print("total modulos => " + str(len(__thg_module__)))

for module in __thg_module__:
    importlib.import_module('.%s' % module, 'THG_libs')
