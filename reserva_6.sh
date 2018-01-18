sudo apt-get --yes --force-yes install firefox=45.0.2+build1-0ubuntu1
cd /home/ubuntu/Browod
sleep 15
nohup python main.py alberto 0 >alberto.log 2>&1 &
sleep 5
nohup python main.py jonas 0 >jonas.log 2>&1 &