import geopandas
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from descartes import PolygonPatch
from shapely.geometry import Point

#####
# UK map

# from:
# https://data.gov.uk/dataset/2aa6727d-c5f0-462a-a367-904c750bbb34/nuts-level-1-january-2018-full-clipped-boundaries-in-the-united-kingdom
gdf = geopandas.read_file("NUTS_Level_1_January_2018_Boundaries.geojson")
ax = gdf["geometry"].plot(facecolor = "white", edgecolor = "black", linewidth = 0.25)

NW = gdf[gdf["nuts118nm"] == "North West (England)"]
NW.plot(ax = ax, facecolor = "#CB6015", edgecolor = "black", linewidth = 0.25)

plt.savefig("UK_NW.svg", bbox_inches='tight')


#####
# NW map
ax = NW.plot(facecolor = "white", edgecolor = "black", linewidth = 0.75)

# here is the data (outer postcode latlongs from: https://www.townscountiespostcodes.co.uk/postcodes/postcode-longitude-and-latitude.php)
groupA_df = pd.read_csv("groupA_points.csv")

# need to make some points
groupA_df['geometry'] = groupA_df.apply(lambda x: Point((x.long, x.lat)), axis = 1)
geo_groupA_df = geopandas.GeoDataFrame(groupA_df, geometry= groupA_df.geometry)

geo_groupA_df.plot(ax = ax, markersize = groupA_df["count"] * 10, color = "#1a505f")

plt.savefig("NW_points.svg", bbox_inches='tight')
