# Libraries
# https://python-graph-gallery.com/163-donut-plot-with-subgroups/
import matplotlib.pyplot as plt
import csv

over = 0
below = 0
just = 0
ov_x = 0
ov_v = 0
be_x = 0
be_v = 0
ju_x = 0
ju_v = 0
total = 0

with open("i11price.csv") as f:
    dic = csv.DictReader(f)
    for row in dic:
        if int(row["price"]) < 35900 - 3590:
            below += 1
            if row["own"] == "1":
                be_v += 1
            else:
                be_x += 1
        elif int(row["price"]) > 35900 + 3590:
            over += 1
            if row["own"] == "1":
                ov_v += 1
            else:
                ov_x += 1
        else:
            just += 1
            if row["own"] == "1":
                ju_v += 1
            else:
                ju_x += 1
        total += 1
print(just, ju_v, ju_x, over, ov_v, ov_x, below, be_v, be_x)

# Make data: I have 3 groups and 7 subgroups
group_names = ['over', 'below', 'just']
group_size = [over, below, just]
subgroup_names = ['own', "don't have", 'own', "don't have", 'own', "don't have"]
subgroup_size = [ov_v, ov_x, be_v, be_x, ju_v, ju_x]

# Create colors
a, b, c = [plt.cm.Purples, plt.cm.GnBu, plt.cm.Oranges]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(over / total), b(below / total), c(just / total)])
plt.setp(mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3 - 0.3, labels=subgroup_names, labeldistance=0.7,
                   colors=[a(ov_v / total), a(ov_x / total),
                           b(be_v / total), b(be_x / total),
                           c(ju_v / total), c(ju_x / total)])
plt.setp(mypie2, width=0.4, edgecolor='white')
plt.margins(0, 0)

fig.savefig("chart.png")
plt.close(fig)
# show it
plt.show()
