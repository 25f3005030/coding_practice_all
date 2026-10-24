'''# Update Ubuntu package repositories
sudo apt update && sudo apt install -y python3-pip python3-venv
# Create a project folder and navigate into it
mkdir -p ~/ubuntu_python_monitor
cd ~/ubuntu_python_monitor

# Create and activate a Python virtual environment
python3 -m venv venv    (venv is name of virutal environoment
source venv/bin/activate  (activate the virual environment 

# Install psutil for Linux system hardware metrics
pip install psutil
'''


hello=1
bye=2
product=hello*bye
print(product)