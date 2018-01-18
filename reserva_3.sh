sudo apt-get --yes --force-yes install firefox=45.0.2+build1-0ubuntu1
cd /home/ubuntu/Browod
sleep 15
nohup python main.py ruben 0 >ruben.log 2>&1 &
sleep 5
nohup python main.py chema 0 >chema.log 2>&1 &
sleep 5
nohup python main.py horacio 0 >horacio.log 2>&1 &