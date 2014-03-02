vagrant-fabric
==============

RHEL [Python Fabric][1] script to setup AWS tools and other dependencies

Requirements
------------
  * root or equivalent
  * Vagrant / VirtualBox 
  * Vagrant box (see below)
  * Python 2.6
  * Python pip
  * Python fabric
  
List of current Vagrant Boxes here:  http://vagrantbox.es/ 

**Getting started with [Vagrant][2] CentOS 6.5 box:**

    vagrant box add centos65-01 https://github.com/2creatives/vagrant-centos/releases/download/v6.5.1/centos65-x86_64-20131205.box
    
    vagrant init centos65-01
    vagrant up
    vagrant ssh

**Getting started with [vagrant-fabric][3]:**

    curl -Os https://raw.github.com/marshyski/vagrant-fabric/master/fabfile.py
    fab -l
    #Only run when vagrant box is up
    fab provision_box
    #Update system when vagrant box is up
    fab upgrade_box


  [1]: http://fabfile.org/
  [2]: http://www.vagrantup.com/
  [3]: https://github.com/marshyski/vagrant-fabric
