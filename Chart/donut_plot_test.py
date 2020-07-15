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

with open("i11price.csv") as f:
    dic = csv.DictReader(f)
    for row in dic:
        if int(row["price"]) < 35900 - 359:
            below += 1
            if row["own"] == "1":
                be_v += 1
            else:
                be_x += 1
        elif int(row["price"]) > 35900 + 359:
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
print(just, ju_v, ju_x, over, ov_v, ov_x, below, be_v, be_x)

# Make data: I have 3 groups and 7 subgroups
group_names = ['over', 'below', 'just']
group_size = [over, below, just]
subgroup_names = ['own', "don't have", 'own', "don't have", 'own', "don't have"]
subgroup_size = [ov_v, ov_x, be_v, be_x, ju_v, ju_x]

# Create colors
a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6), c(0.6)])
plt.setp(mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3 - 0.3, labels=subgroup_names, labeldistance=0.7,
                   colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
plt.setp(mypie2, width=0.4, edgecolor='white')
plt.margins(0, 0)

# show it
plt.show()
