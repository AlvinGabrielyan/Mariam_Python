def defend_wall(wall):
    n = len(wall)
    defended = [False] * n  # List es sarqum, vortex amen tarry False a nerkayacnum iranic, vor heto zut mark anes True-ov

    for i in range(n):
        if wall[i] == 'G': #Ete gtel es G-n, iranic erku hat arajic minchev erku hat heton mark es anum
            if i - 2 >= 0:
                defended[i - 2] = True
            if i - 1 >= 0:
                defended[i - 1] = True
            defended[i] = True
            if i + 1 < n:
                defended[i + 1] = True
            if i + 2 < n:
                defended[i + 2] = True

    return sum(defended) #Hashvuma qez tivna veradardznum function-y

print(defend_wall("-G-G-------")) 
print(defend_wall("----G--G---G-----G---")) 
print(defend_wall("GG---G-----GG---G"))
