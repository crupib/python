
import math
from constants import HEX_SIZE, MAP_COLS, MAP_ROWS, DIRECTIONS

def axial_to_pixel(q,r):
    return int(HEX_SIZE*math.sqrt(3)*(q+r/2)+90), int(HEX_SIZE*1.5*r+80)
def axial_to_screen(q,r,camera_x=0,camera_y=0):
    x,y=axial_to_pixel(q,r); return int(x+camera_x), int(y+camera_y)
def hex_corners(cx,cy):
    return [(cx+HEX_SIZE*math.cos(math.radians(60*i-30)), cy+HEX_SIZE*math.sin(math.radians(60*i-30))) for i in range(6)]
def hex_distance(a,b):
    aq,ar=a; bq,br=b; return int((abs(aq-bq)+abs(aq+ar-bq-br)+abs(ar-br))/2)
def neighbors(q,r):
    return [(q+dq,r+dr) for dq,dr in DIRECTIONS]
def pixel_to_axial(mx,my,camera_x=0,camera_y=0):
    map_x=mx-camera_x; map_y=my-camera_y; best=None; best_dist=999999
    for q in range(MAP_COLS):
        for r in range(MAP_ROWS):
            cx,cy=axial_to_pixel(q,r); d=(map_x-cx)**2+(map_y-cy)**2
            if d<best_dist: best_dist=d; best=(q,r)
    return best


