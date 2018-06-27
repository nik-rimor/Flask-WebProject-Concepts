# -*- mode: ruby -*-
# vi: set ft=ruby :

# $script = <<SCRIPT
# echo I am provisioning...
# date > /etc/vagrant_provisioned_at
# SCRIPT

# Vagrant.configure("2") do |config|
  # config.vm.provision "shell", inline: $script
# end

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.host_name = "web-postgresql"
  config.vm.network :forwarded_port, guest: 8000, host: 8000  

  config.vm.synced_folder ".", "/webproject", create: true
  config.vm.provision :shell, :path => "Vagrant-setup/bootstrap.sh"
  
  # PostgreSQL Server port forwarding
  #config.vm.forward_port 5432, 15432
end
