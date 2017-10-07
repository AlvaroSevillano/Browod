cd /home/ubuntu/Browod
sleep 15
nohup python main.py alberto >alberto.log 2>&1 &
sleep 5
nohup python main.py jonas >jonas.log 2>&1 &