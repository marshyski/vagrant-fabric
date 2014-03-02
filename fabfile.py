#This fabric script must be used with `RHEL/CentOS/Fedora` systems

from fabric.api import sudo, run, env, cd

#Sometimes localhost can't be resolved, using IP instead
env.hosts = ['127.0.0.1']
env.user = 'vagrant'
env.password = 'vagrant'
env.port = 2222

#Run this for the first time on a box to set it up
def provision_box():
    update_system()
    install_epel()
    install_base()
    install_awscli()
    install_python()
    clean_up()

#Run this when you have the need to update the system
def upgrade_box():
    update_system()
    upgrade_awscli()

#Update system via yum
def update_system():
    sudo('yum update --nogpgcheck --skip-broken -y update')    

#Install EPEL repo file
def install_epel():
    sudo('rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')

#Install packages defined below
def yum_install(*packages):
    sudo('yum install --nogpgcheck --skip-broken -y %s' % ' '.join(packages), shell=False)

#Remove packages defined below
def yum_remove(*packages):
    sudo('yum remove -y --skip-broken %s' % ' '.join(packages), shell=False)

#Install dependencies on system via yum 
def install_base():
    yum_install('dos2unix glances screen gcc make python-devel python-setuptools python-pip python-boto euca2ools git')

#Install AWS command-line tools (Python/boto)
def install_awscli():
    sudo('pip install awscli')

#Upgrade pip install of awscli tools
def upgrade_awscli():
    sudo('pip install --upgrade awscli')

#Install Python 2.7.*
def install_python():
    run('curl -Os http://legacy.python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz')
    run('tar xfv Python-2.7.6.tar.xz')
    with cd ('Python-2.7.6'):
        sudo('./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"')
        sudo('make && make altinstall')

#Clean up yum/rpm & post-install of Python 2.7
def clean_up():
    yum_remove('gcc')
    sudo('rm -f /var/lib/rpm/__db*; rpm --rebuilddb')
    sudo('yum history new; yum clean all')
    sudo('rm -rf Python-*')
