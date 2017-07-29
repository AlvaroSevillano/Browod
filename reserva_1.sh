cd /home/ubuntu/Browod
sleep 25
nohup python main_alvaro.py >alvaro.log 2>&1 &
sleep 5
nohup python main_amaya.py >amaya.log 2>&1 &
sleep 6
nohup python main_andoni.py >andoni.log 2>&1 &
nohup python main_koldo.py >koldo.log 2>&1 &