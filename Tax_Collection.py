def collect_taxes(provinces, max_tax, min_tax):
    taxes = {}

    for province in provinces:  # ancnuma dictionary-i amen key, value pair-i vrayov
        wealth = provinces[province]  # vercnum a amen toxi(key,value pair-i miji pair-i) value-n, aysinqn tivy
        tax = wealth * 0.15

        if tax < min_tax:
            tax = 0 
        elif tax > max_tax:
            tax = max_tax  

        taxes[province] = tax #Nor dictionary a sarqum, mejy texadruma amen pair-y, u function-y veradardznuma ed dictionary-n

    return taxes

provinces = {
    'Gaul': 20000,
    'Egypt': 50000,
    'Britannia': 8000,
    'Judea': 4000,
    'Hispania': 15000
}

result = collect_taxes(provinces, 7000, 700)
print(result) 
