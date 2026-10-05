import numpy as np
import pandas as pd

ips = ["192.168.1.10","192.168.1.20","10.0.0.5","10.0.0.8"]
users = ["ali","sara","john","admin","bob"]

start = np.datetime64("2026-01-01")
end = np.datetime64("2026-01-31")

dates = np.arange(start,end)

random_ips = np.random.choice(ips,size=1000)

random_users = np.random.choice(users,size=1000)

random_success = np.random.choice([False,True],size = 1000,p = [0.1,0.9])


random_timestamp = np.random.choice(dates,size =1000)

df = pd.DataFrame({
    "ip" : random_ips,
    "user": random_users,
    "success": random_success,
    "timestamp":random_timestamp

})

df.to_csv("login_logs.csv",index=False)

print(df)
