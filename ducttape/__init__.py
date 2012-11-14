from fabric.api import env

from .package import PackageBase, PackageApt, PackageYum, PackageOpenBSD
from .database import DatabaseBase, DatabaseMySQL, DatabasePostgres, DatabaseSQLite
from .webserver import WebServerBase, WebServerNginx, WebServerApache
from .user import UserBase
from .group import GroupBase
from .ssh import SshBase


class DuctTape(object):

    def __init__(self,
                 package=None,
                 webserver=None,
                 database=None,
                 database_user=None,
                 database_passwd=None):

        env.ducttape = self

        self.opts = {
            'package': {
                'apt': PackageApt,
                'yum': PackageYum,
                'openbsd': PackageOpenBSD,
            },
            'database': {
                'mysql': DatabaseMySQL,
                'postgres': DatabasePostgres,
                'sqlite': DatabaseSQLite,
            },
            'webserver': {
                'nginx': WebServerNginx,
                'apache': WebServerApache
            },

        }

        self.user = UserBase()
        self.group = GroupBase()
        self.ssh = SshBase()

        # setup package
        if package is None:
            self.package = PackageBase()
        else:
            klass = self.opts['package'].get(package)
            if klass is not None:
                self.package = klass()
            else:
                raise Exception('Invalid package option: %s' % package)

        # setup database
        if database is None:
            self.database = DatabaseBase()
        else:
            klass = self.opts['database'].get(database)
            if klass is not None:
                self.database = klass()
            else:
                raise Exception('Invalid database option: %s' % database)

        # setup webserver
        if webserver is None:
            self.webserver = WebServerBase()
        else:
            klass = self.opts['webserver'].get(webserver)
            if klass is not None:
                self.webserver = klass()
            else:
                raise Exception('Invalid webserver option: %s' % webserver)
