cd /home/ubuntu/Browod
sleep 15
nohup python main_risto.py >risto.log 2>&1 &
sleep 5
nohup python main_blas.py >blas.log 2>&1 &