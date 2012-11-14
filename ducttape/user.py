from fabric.api import sudo, hide, puts
from fabric.colors import red


class UserBase(object):

    def passwd(self, user, passwd):
        with hide("running"):
            sudo("echo -e \"%s\\n%s\\n\" | sudo passwd %s" % (passwd, passwd, user))

    def exists(self, name):
        entry = sudo("cat /etc/passwd | egrep '^%s:' ; true" % (name))
        return entry

    def create(self, name, passwd=None, shell="/bin/sh"):
        if self.exists(name):
            puts(red("User %s already exists. Skipping creation" % name))
        else:
            sudo("useradd -m '%s' -s '%s'" % (name, shell))
            if passwd is not None:
                self.passwd(name, passwd)

    def remove(self, name, home=False):
        if self.exists(name):
            sudo("userdel -f %s '%s'" % ("-r" if home else "", name))
