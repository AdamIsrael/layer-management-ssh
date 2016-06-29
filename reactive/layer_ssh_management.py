from charms.reactive import when, set_state, remove_state

from charmhelpers.core.hookenv import config


@when('config.changed.hostname',
      'config.changed.user',
      'config.changed.password',
      )
def configure_ssh_management():
    cfg = config()
    if all(k in cfg for k in ['hostname', 'user', 'password']):
        hostname = cfg['hostname']
        user = cfg['user']
        password = cfg['password']

        if hostname and user and password:
            set_state('mgmt.remote')
            set_state('mgmt.remote.ssh')
        else:
            remove_state('mgmt.remote')
            remove_state('mgmt.remote.ssh')
