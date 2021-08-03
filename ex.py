lat_list = []
lon_list = []



def positionchange(ps):
    ps = 0
    if latitude[ps] - 0.04166667 < position[1] < latitude[ps] + 0.04166667 and longitude[ps] - 0.04166667 < position[2] < longitude[ps] + 0.04166667 :
        ps += 1
    return



