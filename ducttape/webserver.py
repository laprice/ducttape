import os
from fabric.api import sudo
from fabric.contrib.files import exists


class WebServerBase(object):

    def site_enable(self):
        raise Exception('Not Implemented')

    def site_disable(self):
        raise Exception('Not Implemented')


class WebServerApache(WebServerBase):

    def __init__(self,
                 avail_path='/etc/apache2/sites-available/',
                 enabled_path='/etc/apache2/sites-enabled/'):

        self.avail_path = avail_path
        self.enabled_path = enabled_path


class WebServerNginx(WebServerBase):

    def __init__(self,
                 avail_path='/etc/nginx/sites-available/',
                 enabled_path='/etc/nginx/sites-enabled/'):

        self.avail_path = avail_path
        self.enabled_path = enabled_path

    def create_dirs(self):
        if not exists(self.avail_path):
            sudo('mkdir %s' % self.avail_path)
        if not exists(self.enabled_path):
            sudo('mkdir %s' % self.enabled_path)

    def site_enable(self, site):
        site_avail = os.path.join(self.avail_path, site)
        site_enabled = os.path.join(self.enabled_path, site)
        if not exists(site_enabled):
            sudo('ln -s %s %s' % (site_avail, site_enabled))

    def site_disable(self, site):
        site_enabled = os.path.join(self.avail_path, site)
        if exists(site_enabled):
            sudo('rm %s' % site_enabled)
