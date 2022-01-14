import math

points = {
    'N': (100, 80),
    'S': (100, 120),
    'W': (80, 100),
    'E': (120, 100),
}

p2={"A":{"X":106.345,"Y":0.0,"Z":82.953,"ID":0},"B":{"X":118.328,"Y":0.0,"Z":106.343,"ID":1},"C":{"X":93.639,"Y":0.0,"Z":117.828,"ID":2},"D":{"X":81.858,"Y":0.0,"Z":93.774,"ID":3},"One":{"X":96.323,"Y":0.0,"Z":81.898,"ID":4},"Two":{"X":118.194,"Y":0.0,"Z":96.511,"ID":5},"Three":{"X":103.636,"Y":0.0,"Z":118.66,"ID":6},"Four":{"X":80.806,"Y":0.0,"Z":103.281,"ID":7}}
for direction, (x, y) in points.items():
    deg = math.degrees(math.atan2(100 - x, 100 - y))
    print(direction, deg)

for pt, v in p2.items():
    deg = math.degrees(math.atan2(100 - v["X"], 100 - v["Z"]))
    print(pt,'aoe' if (deg + 180) % 90 > 45 else 'tower')
