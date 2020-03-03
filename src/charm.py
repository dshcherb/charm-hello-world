#!/usr/bin/env python3

import logging
import sys

sys.path.append('lib') # noqa

from ops.charm import CharmBase
from ops.framework import StoredState
from ops.main import main
from ops.model import ActiveStatus

logger = logging.getLogger(__name__)


class HelloWorldCharm(CharmBase):

    state = StoredState()

    def __init__(self, *args):
        super().__init__(*args)

        self.state.set_default(logged_hello=False)
        self.framework.observe(self.on.install, self.on_install)

    def on_install(self, event):
        logger.info('Hello, world')
        foo = self.model.config['foo']
        logger.warning(f'Foo config value: {foo}')
        self.model.unit.status = ActiveStatus()


if __name__ == '__main__':
    main(HelloWorldCharm)
