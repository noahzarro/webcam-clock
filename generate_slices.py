from math import sin, cos, pi

base_string = '<mask id="mask{seg_nr}">\n<!-- Only stuff under a white pixel will be visible -->\n<path d="M {center_x}, {center_y} l {out_x} {out_y} L {end_x} {end_y}" fill="white"></path>\n</mask>'
radius = 500
center_x = 960
center_y = 540
degree = 30
rad = degree/180 * pi 

def delta_x(angle):
    return radius*sin(angle)

def delta_y(angle):
    return radius*cos(angle)

ends = []

for i in range(12):
    out_x = delta_x(i*rad)
    out_y = -delta_y(i*rad)

    #print(delta_x((i+1)*rad))
    #print(delta_y((i+1)*rad))

    end_x = center_x + delta_x((i+1)*rad)
    end_y = center_y - delta_y((i+1)*rad)

    ends.append((end_x, end_y))

    segment_mask = base_string.format(seg_nr = i, center_x=center_x, center_y=center_y, out_x=out_x, out_y=out_y, radius=radius, degree=degree, end_x=end_x, end_y=end_y)

    print(segment_mask)



print("<path d=\"M {start_x} {start_y}".format(start_x=center_x+delta_x(0), start_y=center_y-delta_y(0) ))

for end_x, end_y in ends:
    print("L {end_x} {end_y}".format(end_x=end_x, end_y=end_y))

print("\" stroke=\"black\"></path>")
