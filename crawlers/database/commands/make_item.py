# -*- coding: utf-8 -*-
import re
import sys

from items import ItemMakeCommand

from orator.commands.application import application

application.add(ItemMakeCommand())

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(application.run())
