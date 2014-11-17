"""`upload soil data` uses the Remote API to upload the initial data. Once Uplaoded the data is never altered again."""

import AST
from google.appengine.ext import db
from main import SoilFeature


def process_line(line):
    """
    lines consist of the following:
      Soil, Suborder, maxlat, minlat, maxlon, minlon, polygons
    """
    assert len(line.split("\t")) == 8

    soil, suborder, gridID, shape, AST_of_Points, Max_Lat, Min_Lat, Max_Lon, Min_Lon, = line.split("\t")

    #info = lines.split("\t")
    return SoilFeature(
      soil = soil,   suborder = suborder,
      maxlat = Max_Lat, minlat = Min_Lat,
      maxlon = Max_Lon, minlon = Min_Lon,
      #need to fix the polygon processing
      polygon = process_polygon(AST_of_Points)


def process_polygon(x):
    """ Convert the String representation of GeoJSON polygons to a Python List
    Then get the lat/lon values and calcualte min/max

    """
    ast_list = ast.literal_eval(x)
    point_list = list( itertools.chain(*ast_list))
    return point_list


#try this
#https://cloud.google.com/appengine/articles/remote_api#limitations
startingdatafile = "Data/soiltypes.csv"
records = [process_line(line) for line in open(startingdatafile, "r").readlines()]
db.Put(records)