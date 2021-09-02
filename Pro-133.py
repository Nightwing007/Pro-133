from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

import csv
import matplotlib.pyplot as plt
import plotly.express as px

rows = []

with open("Pro-131.csv","r") as f :
  csvR = csv.reader(f)
  for row in csvR :
    rows.append(row)

header = rows[0]
planetData = rows[1:]

header[0] = "Index"

temp_list = list(planetData)

for data in planetData :
  planetMass = data[3]
  if planetMass.lower() == "unknown":
    planetData.remove(data)
    continue
  planetRadius = data[4]
  if planetRadius.lower() == "unknown":
    planetData.remove(data)
    continue

for data in planetData :
    mass = float(data[3]) * 1.989e+30
    data[3] = mass
    radius = float(data[4]) * 6.957e+8
    radius[4] = radius

star_masses = []
star_radiuses = []


for data in planetData :
  star_masses.append(data[3])
  star_radiuses.append(data[4])

X = []
for index, planet_mass in enumerate(star_masses):
  temp_list = [
                  star_radiuses[index],
                  planet_mass
              ]
  X.append(temp_list)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)
    kmeans.fit(X)
    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1, 11), wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()



fig = px.scatter(x=star_radiuses, y=star_masses)
fig.show()