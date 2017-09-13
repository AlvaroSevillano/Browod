cd /home/ubuntu/Browod
sleep 15
nohup python main_andoni.py >andoni.log 2>&1 &
sleep 5
nohup python main_koldo.py >koldo.log 2>&1 &