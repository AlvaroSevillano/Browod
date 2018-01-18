sudo apt-get --yes --force-yes install firefox=45.0.2+build1-0ubuntu1
cd /home/ubuntu/Browod
sleep 15
nohup python main.py alvaro 0 >alvaro.log 2>&1 &
sleep 5
nohup python main.py andoni 0 >andoni.log 2>&1 &