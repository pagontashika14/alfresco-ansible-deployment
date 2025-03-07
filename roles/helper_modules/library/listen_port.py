#!/usr/bin/python
"""
Ansible module to listen on a local INET socket
"""

import socket
import time

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: listen_port
short_description: create socket to listen on custom port
description: create socket to listen on custom port
'''

EXAMPLES = '''
- name: listen on port 8888
  listen_port:
    port: 8888
  async: 10
  poll: 0
'''

def main():
    """listen port main function"""

    fields = {
        "port": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields,supports_check_mode=False)
    response = {"socket": "listen on " + module.params['port']}

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('', int(module.params['port']))
    sock.bind(server_address)
    sock.listen(1)
    while True:
        connection, client_address = sock.accept() # pylint: disable=unused-variable
        time.sleep(5)
        connection.close()
        break
    module.exit_json(changed=True, meta=response)

if __name__ == '__main__':
    main()
