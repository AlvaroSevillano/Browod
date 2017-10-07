cd /home/ubuntu/Browod
sleep 15
nohup python main.py marta >marta.log 2>&1 &
sleep 5
nohup python main.py laura >laura.log 2>&1 &