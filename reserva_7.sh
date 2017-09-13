cd /home/ubuntu/Browod
sleep 15
nohup python main_alberto.py >alberto.log 2>&1 &
sleep 5
nohup python main_jonas.py >jonas.log 2>&1 &