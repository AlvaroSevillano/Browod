cd /home/ubuntu/Browod
sleep 15
nohup python main.py alvaro >alvaro.log 2>&1 &
sleep 5
nohup python main.py amaya >amaya.log 2>&1 &