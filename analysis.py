import pandas as pd
import matplotlib.pyplot as plt

# Read standings data
df = pd.read_csv("standings.csv")

print("\nTEAM STANDINGS DATA\n")
print(df)

# -------- GRAPH 1: Points Distribution --------
plt.figure()
plt.bar(df["Team"], df["Points"])
plt.xlabel("Teams")
plt.ylabel("Points")
plt.title("Tournament Points Distribution")
plt.show()

# -------- GRAPH 2: Wins per Team --------
plt.figure()
plt.bar(df["Team"], df["Wins"])
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.title("Matches Won by Each Team")
plt.show()