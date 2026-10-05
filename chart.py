import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("login_logs.csv")

#print(df)

df["timestamp"] = pd.to_datetime(df["timestamp"])

grouped_timestamp = df[df["success"] == False ].groupby("timestamp").size()

#print(grouped_timestamp)

most_integer = grouped_timestamp.max()

most_failed = grouped_timestamp[grouped_timestamp == most_integer]

print(most_failed)

plt.plot(
   grouped_timestamp.index,
   grouped_timestamp.values
)
plt.xlabel("date")
plt.ylabel("failed logins")
plt.title("failed logins per day")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/failures_per_day.png")
plt.show()


failed_logins = df[df["success"] == False].groupby("ip").size()
#print(failed_logins)


plt.bar(
    failed_logins.index,
    failed_logins.values
)


plt.xlabel("ip source")
plt.ylabel("failed login attempts")
plt.title("failed login attempts per ip")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/failed_attempts_from_ips.png")

plt.show()


failed_users = df[df["success"] == False].groupby("user").size()
print(failed_users)


plt.bar(
    failed_users.index,
    failed_users.values
)

plt.xlabel("user login's attempted")
plt.ylabel("number of failed logins")
plt.title("failed login attempts at each user")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/failed_attempts_at_each_user.png")

plt.show()