cd /home/ubuntu/Browod
sleep 25
nohup python main_alvaro.py >alvaro.log 2>&1 &
sleep 5
nohup python main_amaya.py >amaya.log 2>&1 &
