cd /home/ubuntu/Browod
sleep 15
nohup python main_leixuri.py >leixuri.log 2>&1 &
sleep 5
nohup python main_ana.py >ana.log 2>&1 &