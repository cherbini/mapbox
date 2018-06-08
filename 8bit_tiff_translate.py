from osgeo import gdal
import sys

filename = sys.argv[-1]
src_ds = gdal.Open(filename)

format = "GTiff"
driver = gdal.GetDriverByName(format)

dst_ds = driver.CreateCopy(filename, src_ds, 0)

dst_ds = None
src_ds = None
