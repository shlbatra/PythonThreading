- Allowing threads for another thread to finish. Finish one thread before another
- Ex. Payment system with threads below
- Checkout 
    - Process payment (t1) - 5s
    - Send confirmation email (t2) - 10s
    - Load thank you page (t3) - 3s
Not run t2/t3 till t1 finish. Once t1 done, t2 takes time so would like to run t3 in background while t2 is waiting to connect to server. Lock thread so t1 finishes then t2/t3 start