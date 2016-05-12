# README

This repository is a rewrite of spy611.com

* I started with a windows laptop.

* I replaced windows with Ubuntu 16.04:

* http://releases.ubuntu.com/16.04/ubuntu-16.04-desktop-amd64.iso

* After installation, I enhanced Ubuntu with apt-get shell commands:

```bash
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install autoconf bison build-essential libssl-dev libyaml-dev \
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3       \
libgdbm-dev libsqlite3-dev gitk postgresql postgresql-server-dev-all  \
libpq-dev emacs wget curl chromium-browser openssh-server aptitude    \
ruby ruby-dev sqlite3
```

* Next, I created an account named r5 for my Rails 5 efforts:

```bash
sudo useradd -m -s /bin/bash r5
sudo passwd r5
```

* I logged into r5:

```bash
ssh -YA r5@localhost
```

* In order to install Ruby 2.3.1 I ran some shell commands:

```bash
cd ~
git clone https://github.com/rbenv/rbenv.git      .rbenv
git clone https://github.com/rbenv/ruby-build.git .rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"'               >> ~/.bashrc
bash
rbenv install 2.3.1
rbenv global  2.3.1
gem install bundler
```

* Next I got Postgres ready for Rails:

```bash
sudo su - postgres
psql
CREATE USER     r5 WITH SUPERUSER LOGIN;
ALTER  USER     r5 PASSWORD 'r5';
CREATE DATABASE r5;
CREATE DATABASE v2_development;
^D
^D
```

* Then, I cloned this repository:

```bash
cd ~
git clone https://github.com/danbikle/spy611v2
```

* Next, I used bundler to enhance the repository:

```bash
cd ~/spy611v2
bundle install
```

* Then, I started the Rails webserver on my laptop:

```bash
cd ~/spy611v2
bin/rails server
```

* I used the webserver to serve a page to my browser.

* At that point my dev-env was setup on my laptop.

* I wanted to run spy611v2 on Heroku.

* I created an account on heroku.com

* I installed the heroku-client:

```bash
cd ~
wget https://s3.amazonaws.com/assets.heroku.com/heroku-client/heroku-client.tgz
tar zxf heroku-client.tgz
echo 'export PATH="${HOME}/heroku-client/bin:$PATH"' >> ~/.bashrc
bash
```

* I created an ssh-key for the r5 account:

```bash
ssh-keygen -t rsa
```

* I used the heroku-client to upload the key to heroku:

```bash
heroku keys:add
```

* I used the heroku-client to create an empty app on heroku:

```bash
cd ~/spy611v2
heroku create spy611v2
```

* I filled the empty app with a git push command:

```bash
cd ~/spy611v2
git push heroku master
```

* I used a browser to see the app on heroku.

* If you have questions, e-me (Dan Bikle): bikle101@gmail.com
