import random
import folium 
from folium.plugins import HeatMap

#m = folium.Map(location=[30.5928, 114.3055], zoom_start=9, control_scale=True)
#m.add_child(HeatMap(data=[[30.5928, 114.3055]], radius=15))

def generateData(infectionCount, longitude, latitude):
    list = []
    
    for i in range(infectionCount):
        plusOrMinus = random.randint(0,3)

        if plusOrMinus == 0:
            list.append([longitude + random.uniform(0, .1), latitude + random.uniform(0, .1)])

        if plusOrMinus == 1:
            list.append([longitude + random.uniform(0, .1), latitude - random.uniform(0, .1)])

        if plusOrMinus == 2:
            list.append([longitude - random.uniform(0, .1), latitude - random.uniform(0, .1)])

        if plusOrMinus == 3:
            list.append([longitude - random.uniform(0, .1), latitude + random.uniform(0, .1)])

    return list

if __name__ == "__main__":
    infections = 444;
    longitude = 30.5928
    latitude = 114.3055

    dataPoints = []

    random.seed()

    dataPoints = generateData(infections, longitude, latitude)
    m = folium.Map(location=[30.5928, 114.3055], zoom_start=9, control_scale=True)
    m.add_child(HeatMap(data=dataPoints, radius=15))

    m.save('map.html')