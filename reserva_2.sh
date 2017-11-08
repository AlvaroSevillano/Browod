cd /home/ubuntu/Browod
sleep 15
nohup python main.py leixuri >leixuri.log 2>&1 &
sleep 5
nohup python main.py ana >ana.log 2>&1 &