from charmhelpers.core import hookenv
from charmhelpers.core import unitdata

from charms import reactive
from charms.reactive import when
from charms.reactive import when_not

from shutil import copy2
from subprocess import check_call
from subprocess import CalledProcessError

db = unitdata.kv()
config = hookenv.config()


@when('docker.available')
@when_not('weave.ready')
def install_weave():
    '''
    Place the weave script in $PATH and call it to start the weave
    networking container service
    '''
    copy2('scripts/weave', '/usr/local/bin/weave')
    check_call(['weave', 'launch'])
    reactive.set_state('weave.ready')
    hookenv.status_set('active', 'Weave SDN started')


@when('swarm.ready')
def restart_weave():
    '''
    When swarm starts, it restarts the docker daemon. Use this event
    as an opportunity to ensure the weave container is started
    '''
    try:
        check_call(['weave', 'launch'])
    except CalledProcessError:
        hookenv.log('info', 'Weave restart failed, service is running')
