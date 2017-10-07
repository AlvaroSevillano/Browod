cd /home/ubuntu/Browod
sleep 15
nohup python main.py andoni >andoni.log 2>&1 &
sleep 5
nohup python main.py koldo >koldo.log 2>&1 &