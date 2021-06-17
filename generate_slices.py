from math import sin, cos, pi

base_string = '<mask id="mask{seg_nr}">\n<!-- Only stuff under a white pixel will be visible -->\n<path d="M {center_x}, {center_y} l {out_x} {out_y} L {end_x} {end_y}" fill="white"></path>\n</mask>'
radius = 545
res_x = 1920
res_y = 1080 
center_x = res_x/2
center_y = (res_y/2)-10
degree = 30
rad = degree/180 * pi 
angle_offset_rad = (-15) /180 * pi 
overlap = 8/180 * pi

def delta_x(angle):
    angle += angle_offset_rad
    return radius*sin(angle)

def delta_y(angle):
    angle += angle_offset_rad
    return radius*cos(angle)

starts = []

for i in range(12):
    out_x = delta_x(i*rad)
    out_y = -delta_y(i*rad)

    #print(delta_x((i+1)*rad))
    #print(delta_y((i+1)*rad))

    end_x = center_x + delta_x((i+1)*rad + overlap)
    end_y = center_y - delta_y((i+1)*rad + overlap)

    starts.append((center_x + out_x, center_y + out_y))

    segment_mask = base_string.format(seg_nr = i, center_x=center_x, center_y=center_y, out_x=out_x, out_y=out_y, radius=radius, degree=degree, end_x=end_x, end_y=end_y)

    print(segment_mask)


# segment zero is drawn twice

out_x = delta_x(0)
out_y = -delta_y(0)

end_x = center_x + delta_x(1*rad)
end_y = center_y - delta_y(1*rad)


print(base_string.format(seg_nr = "Perfect", center_x=center_x, center_y=center_y, out_x=out_x, out_y=out_y, radius=radius, degree=degree, end_x=end_x, end_y=end_y))

print("<path d=\"M {start_x} {start_y}".format(start_x=center_x+delta_x(0), start_y=center_y-delta_y(0) ))

for start_x, start_y in starts:
    print("L {start_x} {start_y}".format(start_x=start_x, start_y=start_y))

print("Z \" fill=\"\" stroke=\"black\" fill-opacity=\"0\" stroke-width=\"10\"></path>")
