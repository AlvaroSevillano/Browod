cd /home/ubuntu/Browod
sleep 15
nohup python main_ruben.py >ruben.log 2>&1 &
sleep 5
nohup python main_chema.py >chema.log 2>&1 &