from fabric.api import sudo, puts
from fabric.colors import red


class GroupBase(object):

    def exists(self, name):
        entry = sudo("cat /etc/group | egrep '^%s:' ; true" % (name))
        return entry

    def create(self, name, gid=None):
        opts = []
        if self.exists(name):
            puts(red("Group %s already exists. Skipping creation" % name))
        else:
            if gid:
                opts.append("-g '%s'" % (gid))
            sudo("groupadd %s '%s'" % (" ".join(opts), name))

    def user_add(self, user, groups):
        if isinstance(groups, (list, tuple)):
            for group in groups:
                if not self.exists(group):
                    raise Exception("Group %s doesn't exist" % group)
                sudo("usermod -a -G '%s' '%s'" % (group, user))
        else:
            sudo("usermod -a -G '%s' '%s'" % (groups, user))

    def user_exists(self, user, group):
        pass

    def user_remove(self, user, group):
        pass
