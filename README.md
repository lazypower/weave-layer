# Weave SDN

Weave is a SDN Overlay network for use with containers. This mix in functions
with the `docker layer` to configure docker for launching application containers
on a distributed overlay network.

### Charm Layer

This is a reactive, composable charm layer. In order to generate a charm with
weave networking enabled you must have:

- charm-tools >= 1.6.1

in the `layers.yaml` file, include the weave layer:

    includes: ['layer: docker', 'layer:swarm', 'layer: weave']

Then generate the charm:

    charm refresh -o /path/to/juju_repository

### Deploy the refreshed charm

    juju deploy local:trusty/docker

### Validate that Weave is working

    juju ssh docker/0

    docker run -d --name=pingme ubuntu nc -p 4000 -ll -e echo 'Hello, Weave!'
    docker run -e 'affinity:container!=pingme' --name=pinger -ti ubuntu sh -l
    ping -c3 pingme.weave.local

## Upstream Contact Info

- The [Weave](http://weave.works) project site
- [Weave Works Help & Support](http://weave.works/help/index.html)


