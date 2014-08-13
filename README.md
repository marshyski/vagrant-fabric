vagrant-fabric
==============

RHEL [Python Fabric][1] script to setup AWS tools and other dependencies

Requirements
------------
  * root or equivalent
  * Vagrant / VirtualBox 
  * Vagrant box (see below)
  * Python 2.6/7
  * Python pip
  * Python fabric
  
List of current Vagrant Boxes here:  https://vagrantcloud.com/discover

**Getting started with [Vagrant][2] CentOS 6.5 box:**

    # Downloads box from VagrantCloud
    vagrant box add --provider virtualbox -f puppetlabs/centos-6.5-64-puppet-enterprise
    # Sets up initial Vagrantfile
    vagrant init puppetlabs/centos-6.5-64-puppet-enterprise
    # Turns on local Vagrant box
    vagrant up
    # SSH into newly provisioned Vagrant box
    vagrant ssh

**Getting started with [vagrant-fabric][3]:**

    curl -Osf https://raw.github.com/marshyski/vagrant-fabric/master/fabfile.py
    fab -l #Output:
    clean_up
    gem_install
    gem_update
    install_base
    install_epel
    install_python
    pip_install
    pip_upgrade
    provision_box
    update_system
    yum_install
    yum_remove

    # Only run when vagrant box is up
    fab provision_box
    # yum install example
    fab yum_install:httpd
    # pip install example
    fab pip_install:flask


  [1]: http://fabfile.org/
  [2]: http://www.vagrantup.com/
  [3]: https://github.com/marshyski/vagrant-fabric
