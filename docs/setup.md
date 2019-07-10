Setting up your dev environment! 😀

* Assuming you're on Ubuntu 18.10
	* sudo apt update
	* sudo apt upgrade
* Install virtual box
	* sudo nano /etc/apt/sources.list
	* Find your Ubuntu name (e.g, cosmic, zesty)
	* Append deb https://download.virtualbox.org/virtualbox/debian cosmic contrib
	* wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
	* wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
	* sudo apt update
	* sudo apt install virtualbox-6.0
* Create the VM image (optional)
	* Download Ubuntu 18.04 LTS Desktop from https://www.ubuntu.com/download/desktop
	* Open VirtualBox
	* Create a new virtual machine:
		* Machine > New...
		* Choose Expert Mode
		* Name: lovelace-dev
		* Type: Linux
		* Version: Ubuntu (64-bit)
		* Memory: 2048 MB (can be changed by developer later)
		* Create a virtual hard disk now
			* 128 GB
			* VDI
	* Configure the virtual machine:
		* LovelaceDev > Details > Settings
		* General > Advanced
			* Shared clipboard: bidirectional
			* Drag n' drop: bidirectional
		* System > Processor
			* Processors: 2 CPUs
		* Shared folders
			* Add shared folder...
			* Folder path: ~/lovelace-shared (in the host)
			* Folder name: shared
			* Auto-mount: yes
			* Mount point: /home/ada/shared
	* Install Ubuntu on the virtual machine
		* Start the VM
		* Devices > Optical drives > Pick the Ubuntu .iso
		* Machine > Reset
		* Install Ubuntu
		* Keyboard: English (US)
		* Updates and software:
			* Installation: minimal
			* Update while installing: yes
			* Third-party software: yes
		* Installation
			* Something else
			* Device for boot loader: /dev/sda (64 GB)
			* New partition table on /dev/sda (64 GB)
				* Add partition: 136000 MB, primary, beginning, btrfs, /
				* Add partition: 16000 MB, primary, beginning, btrfs, /lxd-partition
				* Add partition: 1439 MB, primary, beginning, btrfs, /boot
			* New partition table on /dev/sda (64 GB)
				* Add partition: 34360 MB, primary, beginning, btrfs, /lxd-physical-disk
			* Install now
		* Who are you?
			* Name: Ada Lovelace
			* Computer: lovelace-dev-vm
			* Username: ada
			* Log in automatically
		* Username: ada
		* Password: lovelace
		* Automatic login: yes
	* First startup
		* What's new in Ubuntu: next
		* Livepatch: Next
		* Send system info: no
		* Open terminal
		* sudo adduser ada vboxsf  # VERY IMPORTANT!
		* sudo apt update
		* sudo apt upgrade
		* sudo apt install gcc make perl
	* Allow executing sudo without password 
		* sudo visudo
			* Append "ada ALL=(ALL) NOPASSWD: ALL"
		* sudo shutdown now
		* Save a snapshot
	* Install guest additions
		* Start the VM
		* Devices > Insert guest additions...
		* Installer will run, or double click the CD on the desktop
		* Make sure no errors in the output
		* Eject the CD
		* sudo shutdown now
	* Take a snapshot of the VM
		* LovelaceDev > Snapshorts > Take
		* Snapshot name: Ubuntu 18.04 installed with guest additions
		* Start the VM
	* Install essentials packages
		* sudo apt install zsh git ufw gufw wget curl htop tree vim unrar gnome-tweaks fonts-noto-color-emoji
	* Install Oh My ZSH!
		* sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
		* nano ~/.zshrc
			* Change theme to "ys" (https://github.com/robbyrussell/oh-my-zsh/wiki/themes)
			* Add plugins; I really like "z", "sudo", "git", and "extract"
			* touch /home/ada/.z
		* Logout and login to have zsh as the default shell
	* Install Python 3.7 from source
		* https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/
		* sudo apt update
		* sudo apt upgrade
		* sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
		* mkdir /tmp/py && cd /tmp/py && wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz
			* Get latest 3.7 link from https://www.python.org/downloads/source/
		* tar -xf Python-3.7.2.tar.xz
		* cd Python-3.7.2
		* ./configure --enable-optimizations --enable-shared  # CONSIDER USING --prefix TO INSTALL THIS CUSTOM PYTHON IN /lovelace/python3.7
		* make -j 4  # use 4 cores
		* make test
		* sudo make install
		* which python3.7
		* python3.7  # might not work until next step!
		* echo 'export LD_LIBRARY_PATH=/usr/local/lib/' >> ~/.zshrc
		* zsh
		* which python3.7
		* python3.7
		* which pip3
		* pip3 install --user virtualenv
	* Install Python 3.7 via APT
		* sudo apt install python3.7 python3-pip
	* Install miniconda WRONG
		* cd ~/Downloads
		* wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
		* chmod +x Miniconda3-latest-Linux-x86_64.sh
		* ./Miniconda3-latest-Linux-x86_64.sh
		* echo 'export PATH="/home/ada/miniconda3/bin:$PATH"' >> ~/.zshrc
	* Install Apache
		* sudo apt install apache2 apache2-dev
		* sudo systemctl status apache2.service
		* sudo systemctl enable apache2.service
	* Install mod_wsgi from source
		* https://jsephler.co.uk/compile-and-install-pythons-mod_wsgi-for-apache2-in-ubuntu-18-04/
		* cd /opt
		* wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.6.4.tar.gz
		* tar -xzf 4.6.4.tar.gz mod_wsgi-4.6.4/
		* cd mod_wsgi-4.6.4/
	* Install mod_wsgi
		* sudo apt install libapache2-mod-wsgi-py3
	* Install PostgreSQL
		* sudo apt install postgresql postgresql-10 postgresql-contrib
		* sudo systemctl status postgresql.service
		* sudo systemctl enable postgresql.service
	* Install phpPgAdmin
		* sudo apt install phppgadmin
	* Configure PostgreSQL
		* sudo -u postgres -- psql
			* \password postgres
				* Password: lovelace
			* \q
		* sudo -u postgres createuser --interactive
			* Userame: ada
			* Superuser: y
		* sudo -u postgres createdb projectlovelace
		* psql -d projectlovelace
			* \conninfo
			* \q
	* Configure phpPgAdmin
		* nano /etc/apache2/conf-available/phppgadmin.conf
			* Comment out "Require local" and add "Require all granted" for remote access
		* sudo nano /etc/phppgadmin/config.inc.php
			* Set "conf['extra_login_security']" to "false"
		* sudo systemctl restart postgresql
		* sudo systemctl restart apache2
		* firefox http://localhost/phppgadmin/
		* Click on "PostgreSQL" and enter credentials:
			* Username: postgres
			* Password: lovelace
	* Set up LXD
		* sudo apt install lxd lxd-tools
		* sudo usermod --append --groups lxd ada
		* reboot
		* lxd init
			* Cluserting: no
			* Storage pool: yes
				* Name: default-lxd-storage-pool
				* Backend: btrfs
				* Create subvolume: yes
			* MAAS: no
			* Network bridge: yes (this gives containers internet access)
				* Name: lxdbr0
				* IPv4 Address: auto
				* IPv6 Address: auto
			* LXD over the network: no
			* Auto-update stale cached images: yes
		* lxc launch ubuntu:bionic TEST-CONTAINER
		* lxc exec TEST-CONTAINER -- /bin/bash
			* ping google.com
			* exit
		* lxc list
		* lxc delete --force TEST-CONTAINER
		* lxc image list
		* lxc image delete <fingerprint>
	* Install PyCharm
		* Open Ubuntu Software
		* Install PyCharm CE
		* Open Pycharm CE
		* Import settings if possible
	* Miscellaneous
		* Settings > Privacy > Screen Lock > Off
		* Settings > Details > Users and set avatar to Ada Lovelace
	* Finishing up...
		* sudo shutdown now
		* Take a snapshot
		* Done!
* Setup the VM
	* Import the VM
	* Configure the VM
		* Use as much RAM as you can spare
		* Use as many CPUs as possible (I let the VM use all my cores)
		* Use as much video memory as possible
		* Tick 3D acceleration
		* I think applying these video setting changes will fix black screen when maximizing the VM window
		* Check out the other settings
* Environment setup
	* Git
		* git config --global user.name "<name>" (name associated with commits)
		* git config --global user.email "<email>" (email associated with Github account)
		* git config --global core.editor "$(which nano)" (default editor)
	* Create a new SSH key pair
		* ssh-keygen
		* cat ~/.ssh/id_rsa.pub
		* Copy the public key into your GitHub account
	* Clone repos
		* sudo mkdir --mode=777 /lovelace
		* cd /lovelace
		* git clone git@github.com:project-lovelace/lovelace-website.git
		* git clone git@github.com:project-lovelace/lovelace-engine.git
		* git clone git@github.com:basimr/lovelace-problems.git
		* git clone git@github.com:basimr/lovelace-private.git
	* Create log files
		* sudo mkdir --mode=777 /var/log/lovelace
		* sudo touch /var/log/lovelace/lovelace-engine.log /var/log/lovelace/gunicorn-access.log  /var/log/lovelace/gunicorn-error.log  /var/log/lovelace/lovelace-django.log  /var/log/lovelace/lovelace-engine.log
		* sudo chmod 777 /var/log/lovelace/*
	* Environment setup
		* virtualenv --version
			* If command not found:
			* echo 'PATH=$PATH:/home/ada/.local/bin' >> ~/.zshrc && zsh
		* virtualenv --python=/usr/local/bin/python3.7 --prompt='(website-env)' /lovelace/lovelace-website/env
		* source /lovelace/lovelace-website/env/bin/activate
		* pip install django django-registration django-countries django-widget-tweaks
		* pip install psycopg2 requests Pillow
		* pip install uwsgi
		* uwsgi --http :8080 --home /lovelace/lovelace-website/env --chdir /lovelace/lovelace-website/src -w lovelace.wsgi
		* sudo mkdir -p /etc/uwsgi/sites && cd /etc/uwsgi/sites
		* sudo nano lovelace-website.ini
    ```
    [uwsgi]
    project = lovelace-website
    base = /lovelace 

    chdir = %(base)/%(project)/src
    home = %(base)/%(project)/env
    module = lovelace.wsgi:application

    master = true
    processes = 5

    socket = %(base)/%(project)/%(project).sock
    chmod-socket = 664
    vacuum = true
    ```
		* uwsgi --emperor /etc/uwsgi/sites
		* sudo apt install nginx
    * sudo nano /etc/nginx/sites-available/lovelace-website
```
server {
    listen 80;
    server_name projectlovelace.net www.projectlovelace.net;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /lovelace/lovelace-website/src;
    }

    location / {
        include         uwsgi_params;
        uwsgi_pass      unix:/lovelace/lovelace-website/lovelace-website.sock;
    }
}
```
		* sudo ln -s /etc/nginx/sites-available/lovelace-website /etc/nginx/sites-enabled

	* Environment setup
		* virtualenv --version
			* If command not found:
			* echo 'PATH=$PATH:/home/ada/.local/bin' >> ~/.zshrc && zsh
		* pip3 install --user django django-registration django-countries django-widget-tweaks
		* pip3 install --user psycopg2 requests Pillow
		* cd /opt
		* wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.6.4.tar.gz
		* tar -xzf 4.6.4.tar.gz mod_wsgi-4.6.4/
		* cd mod_wsgi-4.6.4/
		* sudo su
		* python3 setup.py install
		* exit
		* mod_wsgi-express start-server
		* Go to localhost:8000
		* 
		*
		* pip3 install virtualenv && zsh
		* mkdir /lovelace/envs && cd /lovelace/envs
		* virtualenv --python=/usr/bin/python3.7 --prompt='(engine-env)' /lovelace/envs/engine
		* echo 'alias website="source /lovelace/envs/website/bin/activate"' >> ~/.zshrc
		* echo 'alias engine="source /lovelace/envs/engine/bin/activate"' >> ~/.zshrc
		* zsh
		* website ; cd /lovelace/lovelace-website
		* pip3 install --user django django-registration django-countries django-widget-tweaks
		* pip3 install --user psycopg2 requests Pillow
		* pip freeze > /lovelace/lovelace-website/requirements.txt
		* deactivate
		* engine ; cd /lovelace/lovelace-engine
		* pip install falcon numpy gunicorn
		* pip freeze > /lovelace/lovelace-engine/requirements.txt
		* deactivate
	* Database setup
		* Download the dump
		* 
	* Conda environments
		* Option 1: Create conda environments from file
			* cd /lovelace/lovelace-engine  && conda env create --file environment.yml
			* cd /lovelace/lovelace-website && conda env create --file environment.yml
		* Option 2: Create conda environments from scratch
			* conda update conda
			* cd /lovelace/lovelace-engine
			* conda create --name engine-env python=3.7
			* source activate engine-env
			* conda install numpy gunicorn
			* pip install falcon
			* conda env export > environment.yml
			* source deactivate
			* cd /lovelace/lovelace-website
			* conda create --name website-env python=3.7
			* source activate website-env
			* pip install django django-registration django-countries django-widget-tweaks
			* pip install psycopg2 requests Pillow
			* conda env export > environment.yml
			* source deactivate
		* Option 2A: Create conda environments from scratch
			* conda update conda
			* cd /lovelace/lovelace-engine
			* conda create --name engine-env python=3.7
			* source activate engine-env
			* conda install numpy gunicorn
			* pip install falcon
			* conda env export > environment.yml
			* source deactivate
			* cd /lovelace/lovelace-website
			* conda create --name website --p /lovelace/envs/website python=3.7
			* source activate /lovelace/envs/website
			* pip install django django-registration django-countries django-widget-tweaks
			* pip install psycopg2 requests Pillow
			* conda env export > environment.yml
			* source deactivate
	* Configure Apache
		* sudo systemctl stop apache2.service
		* cd /etc/apache2/
		* sudo mv apache2.conf apache2.conf.DEFAULT
		* sudo mv envvars envvars.DEFAULT
		* sudo mv ports.conf ports.conf.DEFAULT
		* sudo cp /lovelace/lovelace-website/conf_stash/dev/apache2.conf ./
		* sudo cp /lovelace/lovelace-website/conf_stash/envvars ./
		* sudo cp /lovelace/lovelace-website/conf_stash/dev/ports.conf ./
		* sudo cp /lovelace/lovelace-website/conf_stash/dev/projectlovelace.net.conf ./sites-available
		* sudo ln -s /etc/apache2/sites-available/projectlovelace.net.conf /etc/apache2/sites-enabled/projectlovelace.net.conf
		* sudo rm sites-enabled/000-default.conf
		* sudo apache2ctl configtest
		* Make sure paths in wsgi.py are correct
* sudo mkdir /var/www/projectlovelace.net
* sudo ln -s /lovelace-website /var/www/projectlovelace.net/lovelace-website
/home/ada/miniconda3/envs/engine-env
/home/ada/miniconda3/envs/website-env

* Final thoughts
	* Snapshot your VM regularly
	* Backup your VM
	* Commit often
