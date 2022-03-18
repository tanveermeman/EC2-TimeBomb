# EC2-TimeBomb
Time ticking BOMB to terminate temporary EC2 instances 
Problem Statement: Terminate an instance if it exceeds TTL. 

ec2-timebomb runs as a periodic job on AWS Lambda

Algorithm
1. List all regions
2. For every region
    a. List all ec2-instances
    b. For every ec2-instance
        1. Calculate Uptime (Using `LaunchTime`)
        2. If Uptime > TTL
        3. Destroy ec2-instance

Deployment Steps
Step1
Step2


Dependencies
 IAM role with following access
  1. List instances
  2. Read instance tags
  3. Destroy instances
 Todo
  1. Deploy Lambda using 
  2. AWS console
  3. AWS cli
  4.Terraform


