briff    = [0,  0,   2,       2,   -5,      -4,   -4,    3,    3,  3,  -2, -1.5, -1, 1]
briffdur = [1/2,1/2, rest(1), 1/2, rest(1), 1/2,  1/2, rest(1),1/2,1/2,1/4,1/4,  1/2,1/2]
bintro =    [-3,  -2,  -1,  1]
bintrodur = [1, 1, 1, 1]

print(SynthDefs)
print(Samples)

p1 >> bass(briff, dur=briffdur)

c = P(0, 3, 5)
p3 >> blip([c, c,c,c, c, c+1,c, c, c, c],
    dur=[1, rest(1/2), 1/2, 1/2, rest(1/2), 1, 1/2, 1/2, 1/2, rest(1/2)],
    amplify=0.3,
    blur=1).every(8, "offadd", 2)
    
p4 >> play("uu~o[uu](o//)uo", amplify=0.3, )

p4 >> play(" h", dur=[rest(2), 1,])

print(FxList)

p4 >> play("$y^^($h)z$x")

print(bintro + briff)
