from fabric.api import sudo


class PackageBase(object):
    def update(self):
        raise Exception('Not Implemented')

    def upgrade():
        raise Exception('Not Implemented')

    def install():
        raise Exception('Not Implemented')


class PackageOpenBSD(PackageBase):
    pass


class PackageYum(PackageBase):
    pass


class PackageApt(PackageBase):

    def add_repo(self, repo):
        self.install('python-software-properties', quiet=True)
        sudo('add-apt-repository "%s"' % repo)
        self.update()

    def update(self):
        sudo('apt-get update')

    def upgrade(self, update=False, quiet=False):
        if update:
            self.update()
        cmd = "%s apt-get %s upgrade" % (
            "DEBIAN_FRONTEND=noninteractive" if quiet else "",
            "--yes" if quiet else ""
        )
        sudo(cmd)

    def install(self, packages, quiet=False):

        if isinstance(packages, (list, tuple)):
            packages = " ".join(packages)

        cmd = "%s apt-get %s install %s %s" % (
            "DEBIAN_FRONTEND=noninteractive" if quiet else "",
            "--yes" if quiet else "",
            "--force-yes" if quiet else "",
            packages
        )
        sudo(cmd)
