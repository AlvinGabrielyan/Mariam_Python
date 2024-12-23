import math

def aqueduct_length(segments):
    total_length = 0.0

    for horizontal, vertical in segments:
        vertical_km = vertical / 1000.0 #sa metrov a tvac, sarqum es kilometr
        segment_length = math.sqrt(horizontal**2 + vertical_km**2)
        #kam karas 8-rd toxi poxaren gres:(es depqum mth import ches anum) segment_length = (horizontal**2 + vertical_km**2)**0.5
        total_length += segment_length

    return round(total_length, 3)


segments = [(2, 10), (3, -5), (1.5, 15), (2.5, -10)]
print(aqueduct_length(segments))  
