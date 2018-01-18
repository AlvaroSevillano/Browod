sudo apt-get --yes --force-yes install firefox=45.0.2+build1-0ubuntu1
cd /home/ubuntu/Browod
sleep 15
nohup python main.py leixuri 0 >leixuri.log 2>&1 &
sleep 5
nohup python main.py ana 0 >ana.log 2>&1 &
sleep 5
nohup python main.py marta_chema 0 >marta_chema.log 2>&1 &