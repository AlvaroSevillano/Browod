cd /home/ubuntu/Browod
sleep 15
nohup python main_marta.py >marta.log 2>&1 &
sleep 5
nohup python main_laura.py >laura.log 2>&1 &