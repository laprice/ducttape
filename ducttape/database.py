from fabric.api import run, puts
from fabric.colors import green


class DatabaseBase(object):

    def change_passwd(self):
        raise Exception('Not Implemented')


class DatabaseMySQL(DatabaseBase):

    def change_passwd(self, user, passwd):
        # TODO: `mysqladmin` only changes current suser. Pipe from echo
        # to `mysql`.
        puts(green('Current MySQL %s passwd [Enter for blank]:' % user))
        run('mysqladmin -u %s -p password %s' % (user, passwd))


class DatabasePostgres(DatabaseBase):
    pass


class DatabaseSQLite(DatabaseBase):
    pass
