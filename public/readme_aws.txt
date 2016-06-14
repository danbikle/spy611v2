~/spy611v2/public/readme_aws.txt

I followed these steps to deploy spy611 to my AWS account.

- Go to AWS console for Oregon:
  - https://us-west-2.console.aws.amazon.com
- Create AWS account
- Or login to existing AWS account
- Navigate to Oregon region in upper right corner:
  - https://us-west-2.console.aws.amazon.com
- Click EC2 link in upper left corner:
  - https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2
- Click Launch Instance blue button
- Click Community AMIs on left side.
- Search for this AMI:
  - ub4TSDS443sshd
- If you find it, Click blue Select button on right side.
- Specify you want a t2.medium instance with 4GB of Memory.
- Click Next: Configure ...
- Click Next: Add Storage
- Click Next: Tag Instance
- Click Next: Configure Security ...
  - Click Add Rule:
    - Custom TCP Rule:
      - HTTPS (about 1/2 way down)
  - Click Add Rule:
    - Custom TCP Rule:
      - Put 2016 in port-range-field
      - Set source to 'anywhere'
- Intent above is to open ports 443 and 2016
- I want to use 443 for ssh-traffic
- I want to use 2016 for web-server traffic
- Click Review Launch blue botton
- Click Launch blue botton
- Create (or pick existing) PEM key
- I should see 'Launching' message from AWS.
- While waiting for launch, copy the key to ~/.ssh/tsds.pem:
  - mkdir -p ~/.ssh/
  - cp ~/Downloads/whatever.pem ~/.ssh/tsds.pem
  - chmod 600 ~/.ssh/tsds.pem
- After launch, note the Public IP address of the new instance.
  - I should see something like this:
    - 54.201.123.142

- After launch, create (or update) ~/.ssh/config with syntax like this:

ServerAliveInterval 30
ServerAliveCountMax 4
Host uws  
  HostName 54.201.123.142
  Port 443
  IdentityFile ~/.ssh/tsds.pem
  User ubuntu

- I should be able to login with simple shell command:
  - ssh uws
  
- I should see something like this:

r5@al78:~ $ 
r5@al78:~ $ ssh uws
Warning: Permanently added '[54.201.123.142]:443' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-74-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Tue Jun 14 01:24:42 UTC 2016

  System load: 0.15               Memory usage: 1%   Processes:       87
  Usage of /:  13.2% of 29.39GB   Swap usage:   0%   Users logged in: 0

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud


Last login: Mon Jun 13 23:24:59 2016 from c-98-207-170-101.hsd1.ca.comcast.net
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$


- I should verify that Python works:

ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ python
Python 3.5.1 |Anaconda 4.0.0 (64-bit)| (default, Dec  7 2015, 11:16:01) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> quit()
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$

- I should verify that Ruby works:

ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ ruby -v
ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-linux]
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$

- I should verify that Postgres works:

ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ psql
psql (9.3.13)
Type "help" for help.

ubuntu=# 
ubuntu=# \q
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$

- I should verify that Rails works:

ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ cat ~/spy611v2/script/railss2016.bash
#!/bin/bash

# ~/spy611v2/script/railss2016.bash

# This script should start rails webserver on all interfaces which then listen on port 2016.

cd $HOME
cd spy611v2
bin/rails s -p 2016 -b 0.0.0.0
exit
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ ~/spy611v2/script/railss2016.bash
=> Booting Puma
=> Rails 5.0.0.rc1 application starting in development on http://0.0.0.0:2016
=> Run `rails server -h` for more startup options
DEPRECATION WARNING: Using a dynamic :controller segment in a route is deprecated and will be removed in Rails 5.1. (called from block in <top (required)> at /home/ubuntu/spy611v2/config/routes.rb:11)
DEPRECATION WARNING: Using a dynamic :action segment in a route is deprecated and will be removed in Rails 5.1. (called from block in <top (required)> at /home/ubuntu/spy611v2/config/routes.rb:11)
Puma starting in single mode...
* Version 3.4.0 (ruby 2.3.1-p112), codename: Owl Bowl Brawl
* Min threads: 5, max threads: 5
* Environment: development
* Listening on tcp://0.0.0.0:2016
Use Ctrl-C to stop


- I should see a copy of spy611.com at http://myip:2016
  - For example: http://54.201.123.142:2016


- I should verify that spy611 python scripts work:
  - cd ~/spy611v2/script
  - cat night.bash
  - ./night.bash
  
- I should see something like this:

ubuntu@ip-172-30-0-57:~/spy611v2/script$ 
ubuntu@ip-172-30-0-57:~/spy611v2/script$ cd ~/spy611v2/script
ubuntu@ip-172-30-0-57:~/spy611v2/script$ 
ubuntu@ip-172-30-0-57:~/spy611v2/script$ ./night.bash
--2016-06-14 02:03:38--  http://ichart.finance.yahoo.com/table.csv?s=%5EGSPC
Resolving ichart.finance.yahoo.com (ichart.finance.yahoo.com)... 208.71.44.30, 208.71.44.31, 2001:4998:c:401::c:9102, ...
Connecting to ichart.finance.yahoo.com (ichart.finance.yahoo.com)|208.71.44.30|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/csv]
Saving to: ‘/tmp/GSPC.csv’

    [  <=>                                  ] 1,204,327   4.13MB/s   in 0.3s   

2016-06-14 02:03:38 (4.13 MB/s) - ‘/tmp/GSPC.csv’ saved [1204327]

I am building features from this file:
GSPC2.csv
Busy...
Done...
I am building CSV files from this file:
ftrGSPC2.csv
Busy...
Done.
/home/ubuntu/anaconda3/lib/python3.5/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
/home/ubuntu/anaconda3/lib/python3.5/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
  warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
New png file: 
plot1981.png
New png file: 
plot1982.png
New png file: 
plot1983.png
New png file: 
plot1984.png
New png file: 
plot1985.png
New png file: 
plot1986.png
New png file: 
plot1987.png
New png file: 
plot1988.png
New png file: 
plot1989.png
New png file: 
plot1990.png
New png file: 
plot1991.png
New png file: 
plot1992.png
New png file: 
plot1993.png
New png file: 
plot1994.png
New png file: 
plot1995.png
New png file: 
plot1996.png
New png file: 
plot1997.png
New png file: 
plot1998.png
New png file: 
plot1999.png
New png file: 
plot2000.png
New png file: 
plot2001.png
New png file: 
plot2002.png
New png file: 
plot2003.png
New png file: 
plot2004.png
New png file: 
plot2005.png
New png file: 
plot2006.png
New png file: 
plot2007.png
New png file: 
plot2008.png
New png file: 
plot2009.png
New png file: 
plot2010.png
New png file: 
plot2011.png
New png file: 
plot2012.png
New png file: 
plot2013.png
New png file: 
plot2014.png
New png file: 
plot2015.png
New png file: 
plot2016.png
ubuntu@ip-172-30-0-57:~/spy611v2/script$ 
ubuntu@ip-172-30-0-57:~/spy611v2/script$ 
ubuntu@ip-172-30-0-57:~/spy611v2/script$

- I should create ssh-keys so I can deploy my site to heroku:
  - When it asks me for a passphrase I should just press enter-key:
    - ssh-keygen -t rsa

- I should see something like this:

ubuntu@ip-172-30-0-57:~/spy611v2/script$ 
ubuntu@ip-172-30-0-57:~/spy611v2/script$ cd ~
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ ls -la .ssh/
total 12
drwx------  2 ubuntu ubuntu 4096 Jun 13 22:21 .
drwxr-xr-x 13 ubuntu ubuntu 4096 Jun 14 01:54 ..
-rw-------  1 ubuntu ubuntu  779 Jun 14 01:24 authorized_keys
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/.ssh/id_rsa.
Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub.
The key fingerprint is:
25:af:4f:86:c7:37:e6:c7:2c:64:a8:6d:7a:51:eb:f6 ubuntu@ip-172-30-0-57
The key's randomart image is:
+--[ RSA 2048]----+
|                 |
|                 |
|        . .      |
|         +  .    |
|        S .o .   |
|         +o +    |
|        oo==+o   |
|        .=+++.+  |
|        .+...+E  |
+-----------------+
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$ ls -la .ssh/
total 20
drwx------  2 ubuntu ubuntu 4096 Jun 14 02:09 .
drwxr-xr-x 13 ubuntu ubuntu 4096 Jun 14 01:54 ..
-rw-------  1 ubuntu ubuntu  779 Jun 14 01:24 authorized_keys
-rw-------  1 ubuntu ubuntu 1679 Jun 14 02:09 id_rsa
-rw-r--r--  1 ubuntu ubuntu  403 Jun 14 02:09 id_rsa.pub
ubuntu@ip-172-30-0-57:~$ 
ubuntu@ip-172-30-0-57:~$

- I should use a laptop-browser to create an account at heroku.com

- I should prepare for heroku deployment:
  - cd ~/spy611v2
  - heroku auth:login
  - heroku create spy20160613
    - spy20160613 is unique
    - you should pick a different name
  - heroku keys:add
  - git push heroku master

- I should see something like this:
remote:        Asset precompilation completed (4.94s)        
remote:        Cleaning assets        
remote:        Running: rake assets:clean        
remote: 
remote: -----> Discovering process types        
remote:        Procfile declares types     -> web        
remote:        Default types for buildpack -> console, rake, worker        
remote: 
remote: -----> Compressing...        
remote:        Done: 60.5M        
remote: -----> Launching...        
remote:        Released v5        
remote:        https://spy20160613.herokuapp.com/ deployed to Heroku        
remote: 
remote: Verifying deploy... done.        
To https://git.heroku.com/spy20160613.git
 * [new branch]      master -> master
ubuntu@ip-172-30-0-57:~/spy611v2$ 
ubuntu@ip-172-30-0-57:~/spy611v2$

- I should see a copy of spy611.com here:
  - https://spy20160613.herokuapp.com/

- That completes the AWS, TSDS, spy611.com Demo.
- If you have questions e-me:
  - bikle101@gmail.com
  
