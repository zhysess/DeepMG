import json
import sys
sys.path.append('/Users/didi/DeepMG/')
sys.path.append('../tptk/')
from tptk.common.road_network import load_rn_shp
from tptk.common.trajectory import parse_traj_file
from tptk.common.grid import Grid
from tptk.common.mbr import MBR
from tptk.common.spatial_func import distance, bearing, LAT_PER_METER

rn = load_rn_shp('')
with open('../data/tdrive_sample/conf_tdrive_sample.json', 'r') as f:
    conf = json.load(f)
    print(conf)
