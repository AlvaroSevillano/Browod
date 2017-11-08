cd /home/ubuntu/Browod
sleep 15
nohup python main.py risto >risto.log 2>&1 &
sleep 5
nohup python main.py blas >blas.log 2>&1 &