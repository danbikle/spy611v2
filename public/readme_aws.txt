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
  
