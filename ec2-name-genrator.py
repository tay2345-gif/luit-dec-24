import random
import string 

# authorize department
department_ = input ("what department are you in ?")

# number of instances 
num_instances = int (input ("how many EC2 instances you need"))

# create unique names
for x in range(num_instances):
    nice_ec2 = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    
    #ec2 names
    ec2_ =f"{department_}-{nice_ec2}"
    print(f"Ec2 instance {x+1} name {ec2_}")