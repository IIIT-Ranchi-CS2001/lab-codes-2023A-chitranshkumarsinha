import matplotlib.pyplot as plt
parties_mp = ['BJP', 'INC', 'BSP', 'Others']
seats_mp = [163, 66, 0, 1]
total_seats_mp = sum(seats_mp)
seat_share_mp = [seat / total_seats_mp * 100 for seat in seats_mp]
parties_rj = ['INC', 'BJP', 'BSP', 'Others']
seats_rj = [69, 115, 2, 13]
total_seats_rj = sum(seats_rj)
seat_share_rj = [seat / total_seats_rj * 100 for seat in seats_rj]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))
ax1.pie(seat_share_mp, labels=parties_mp, autopct='%1.1f%%', startangle=90, colors=colors,
        explode=[0.1 if max(seat_share_mp) == share else 0 for share in seat_share_mp])
ax1.set_title("Madhya Pradesh Assembly Election 2023")
ax2.pie(seat_share_rj, labels=parties_rj, autopct='%1.1f%%', startangle=90, colors=colors,
        explode=[0.1 if max(seat_share_rj) == share else 0 for share in seat_share_rj])
ax2.set_title("Rajasthan Assembly Election 2023")
plt.tight_layout()
fig, ax3 = plt.subplots(figsize=(10, 6))
x = range(len(parties_mp))
bar_width = 0.35
ax3.bar(x, seats_mp, width=bar_width, label='Madhya Pradesh', color='blue')
ax3.bar([i + bar_width for i in x], seats_rj, width=bar_width, label='Rajasthan', color='green')
ax3.set_xlabel("Parties")
ax3.set_ylabel("Seats Won")
ax3.set_title("Assembly Elections 2023: Seats Won in Madhya Pradesh & Rajasthan")
ax3.set_xticks([i + bar_width/2 for i in x])
ax3.set_xticklabels(parties_mp)
ax3.legend()
plt.tight_layout()
plt.show()