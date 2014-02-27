#This fabric script must be used with `RHEL/CentOS/Fedora` systems

from fabric.api import *

# Sometimes localhost can't be resolved, using ip instead.
env.hosts = ['127.0.0.1']
env.user = 'vagrant'
env.password = 'vagrant'
env.port = 2222

def provision_box():
    update_system()
    install_epel()
    install_base()
    install_python()
    clean_up()

def update_system():
    sudo('yum update --nogpgcheck --skip-broken -y update')    

def install_epel():
    sudo('rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')

def yum_install(*packages):
    sudo('yum install --nogpgcheck --skip-broken -y %s' % ' '.join(packages), shell=False)

def yum_remove(*packages):
    sudo('yum remove -y %s' % ' '.join(packages), shell=False)

def install_base():
    yum_install('dos2unix glances screen gcc make python-devel python-setuptools python-pip python-boto euca2ools')

def install_python():
    run('curl -O http://python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz')
    run('tar xfv Python-*')
    with cd('Python-*'):
        sudo('./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"')
        sudo('make && make altinstall')

def clean_up():
    yum_remove('gcc make')
    sudo('rm -f /var/lib/rpm/__db*; rpm --rebuilddb; yum history new; yum clean all')
    run('rm -rf Python-*')
