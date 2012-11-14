import os
from fabric.api import run
from fabric.contrib.files import append, exists


class SshBase(object):

    def create_ssh_folder(self):
        if not exists('~/.ssh'):
            run('mkdir ~/.ssh')
            run('chmod 700 ~/.ssh')
            run('touch ~/.ssh/authorized_keys')
            run('chmod 600 ~/.ssh/authorized_keys')

    def authorize(self, user, local_keyfile):
        self.create_ssh_folder()
        keyfile = os.path.expanduser('~/.ssh/%s' % local_keyfile)

        with open(keyfile) as f:
            key = f.read()

        append('~/.ssh/authorized_keys', key)
