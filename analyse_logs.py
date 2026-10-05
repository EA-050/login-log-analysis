import pandas as pd

df = pd.read_csv("login_logs.csv")

#print(df)

missing = df.isna().sum()

failed_logins = df[df["success"] == False].groupby("ip").size()

users_failed = df[df["success"] == False].groupby("user").size()

mean_failed = failed_logins.mean()

std_failed = failed_logins.std()

z_score = (failed_logins - mean_failed) / std_failed 

suspicious_ip = failed_logins[z_score >= 2] #catches brute force attacks above/at 2 z score
#print(suspicious_ip)
                                            
most_failed = users_failed.idxmax() # gives the name of the most attacked user

print(most_failed)
                                                #find the most target user
target_user_rows = df[df["user"] == most_failed] 

#print(target_user_rows)

#from the most targeted user, gets only the rows which are false.
failed_target_user = df[(df["success"] == False) & (df["user"] == most_failed)]

#print(failed_target_user)

#number of failed attempts per ip
attempts = failed_target_user.groupby("ip").size()

print(attempts)

#the targetuser's failed rows is grouped by ip, finds the ip with the most failed attempts
most_failed_attempts = failed_target_user.groupby("ip").size().max()

#print(most_failed_attempts)

#find the ips with the most failed attempts and saves as bool
most_failed_ip = (attempts == most_failed_attempts)

#print(most_failed_ip)

#find ips with the most failures on the most targeted user
find_ip = attempts[most_failed_ip == True]
print(find_ip)

df["timestamp"] = pd.to_datetime(df["timestamp"]) 

#failures per day
per_day = df[df["success"] == False].groupby("timestamp").size()

#print(per_day)

#max failure 
max_per_day = per_day.max()

max_days = per_day[per_day == max_per_day]
print(max_days)