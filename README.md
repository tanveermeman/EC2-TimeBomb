# EC2-TimeBomb
Time ticking BOMB to terminate temporary EC2 instances 
Problem Statement: Terminate an instance if it exceeds TTL. ec2-timebomb runs as a periodic job on AWS Lambda

Algorithm
List all regions
For every region
List all ec2-instances
For every ec2-instance
Calculate Uptime (Using `LaunchTime`)
If Uptime > TTL
Destroy ec2-instance

Deployment Steps
Step1
Step2


Dependencies
IAM role with following access
List instances
Read instance tags
Destroy instances
Todo
Deploy Lambda using 
AWS console
AWS cli
Terraform


