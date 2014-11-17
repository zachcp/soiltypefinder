"""`upload soil data` uses the Remote API to upload the initial data. Once Uplaoded the data is never altered again."""

from google.appengine.ext import db
from main import SoilFeature


def process_line(line):
    """
    lines consist of the following:
      Soil, Suborder, maxlat, minlat, maxlon, minlon, polygons
    """
    assert len(line.split("\t")) == 8

    info = lines.split("\t")
    return SoilFeature(
      soil = info[0],   suborder = info[1],
      maxlat = info[2], minlat = info[3],
      maxlon = info[4], minlon = info[5]
      #need to fix the polygon processing
      polygon = [ p for p in info[6] ] )
    
#try this
#https://cloud.google.com/appengine/articles/remote_api#limitations
startingdatafile = "data/soiltypes.csv"
records = [process_line(line) for line in open(startingdatafile, "r").readlines()]
db.Put(records)