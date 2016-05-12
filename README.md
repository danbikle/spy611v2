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

* When I git pull recent changes to the repository, I use these shell commands:

```bash
cd ~/spy611v2
git pull origin master
bundle install
```

* Here is a demo screen dump:

```bash
r5@nia111:~ $ 
r5@nia111:~ $ 
r5@nia111:~ $ cd ~/spy611v2
r5@nia111:~/spy611v2 $ 
r5@nia111:~/spy611v2 $ git pull origin master
Warning: Permanently added 'github.com,192.30.252.128' (RSA) to the list of known hosts.
remote: Counting objects: 4, done.        
remote: Compressing objects: 100% (1/1), done.        
remote: Total 4 (delta 3), reused 4 (delta 3), pack-reused 0        
Unpacking objects: 100% (4/4), done.
From github.com:danbikle/spy611v2
 * branch            master     -> FETCH_HEAD
   0f30125..84e200c  master     -> origin/master
Updating 0f30125..84e200c
Fast-forward
 Gemfile      | 28 +++++++++++++---------------
 Gemfile.lock | 33 +++++++++++++++++++++++++++++++++
 2 files changed, 46 insertions(+), 15 deletions(-)
r5@nia111:~/spy611v2 $ 
r5@nia111:~/spy611v2 $ 
r5@nia111:~/spy611v2 $ bundle install
Using rake 11.1.2
Using concurrent-ruby 1.0.2
Using i18n 0.7.0
Using minitest 5.8.4
Using thread_safe 0.3.5
Using builder 3.2.2
Using erubis 2.7.0
Using mini_portile2 2.0.0
Using json 1.8.3
Using nio4r 1.2.1
Using websocket-extensions 0.1.2
Using mime-types-data 3.2016.0221
Using arel 7.0.0
Using byebug 9.0.0
Using coffee-script-source 1.10.0
Using execjs 2.6.0
Using method_source 0.8.2
Using thor 0.19.1
Using debug_inspector 0.0.2
Using ffi 1.9.10
Using tilt 2.0.2
Using sexp_processor 4.7.0
Using multi_json 1.12.0
Using libv8 3.16.14.15
Using rb-fsevent 0.9.7
Using pg 0.18.4
Using puma 3.4.0
Using bundler 1.12.3
Using rails_serve_static_assets 0.0.5
Using rails_stdout_logging 0.0.5
Using ref 2.0.0
Using sass 3.4.22
Using spring 1.7.1
Using turbolinks-source 5.0.0.beta4
Using tzinfo 1.2.2
Using nokogiri 1.6.7.2
Using rack 2.0.0.rc1
Using websocket-driver 0.6.3
Using mime-types 3.0
Using coffee-script 2.4.1
Using uglifier 3.0.0
Using rb-inotify 0.9.7
Using haml 4.0.7
Using ruby_parser 3.8.2
Using rails_12factor 0.0.3
Using therubyracer 0.12.2
Using turbolinks 5.0.0.beta2
Using activesupport 5.0.0.rc1
Using loofah 2.0.3
Using rack-test 0.6.3
Using sprockets 3.6.0
Using mail 2.6.4
Using listen 3.0.7
Using html2haml 2.0.0
Using rails-deprecated_sanitizer 1.0.3
Using globalid 0.3.6
Using activemodel 5.0.0.rc1
Using jbuilder 2.4.1
Using rails-html-sanitizer 1.0.3
Using spring-watcher-listen 2.0.0
Using rails-dom-testing 1.0.7
Using activejob 5.0.0.rc1
Using activerecord 5.0.0.rc1
Using actionview 5.0.0.rc1
Using actionpack 5.0.0.rc1
Using actioncable 5.0.0.rc1
Using actionmailer 5.0.0.rc1
Using railties 5.0.0.rc1
Using sprockets-rails 3.0.4
Using coffee-rails 4.1.1
Using haml-rails 0.9.0
Using jquery-rails 4.1.1
Using web-console 3.1.1
Using rails 5.0.0.rc1
Using sass-rails 5.0.4
Bundle complete! 19 Gemfile dependencies, 75 gems now installed.
Use `bundle show [gemname]` to see where a bundled gem is installed.
r5@nia111:~/spy611v2 $ 
r5@nia111:~/spy611v2 $ 
r5@nia111:~/spy611v2 $ 
```

* If you have questions, e-me (Dan Bikle): bikle101@gmail.com
