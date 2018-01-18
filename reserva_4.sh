sudo apt-get --yes --force-yes install firefox=45.0.2+build1-0ubuntu1
cd /home/ubuntu/Browod
sleep 15
nohup python main.py javi 0 >javi.log 2>&1 &
sleep 5
nohup python main.py laura 0 >laura.log 2>&1 &