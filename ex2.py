import turtle as tu

door = [
    ['set', (20,0)],
    ['rt', -90],
    ['fd', 40],
    ['rt', 90],
    ['fd', 40],
    ['rt', 90],
    ['fd', 40],
]

wall = [
    ['set', (20,0)],
    ['sh', 180],
    ['fd', 20],
    ['rt', 90],
    ['fd', 80],
    ['rt', 90],
    ['fd', 80],
    ['rt', 90],
    ['fd', 80],
    ['rt', 90],
    ['fd', 60],
]

roof = [
    ['set', (0,80)],
    ['sh', 0],
    ['rt', -60],
    ['fd', 80],
    ['rt', -(360 - 120)],
    ['fd', 80],
]

zones = {
    'door': {'color': 'red', 'layout': door},
    'wall': {'color': 'black', 'layout': wall},
    'roof': {'color': 'green', 'layout': roof},
}

for zone,details in zones.items():
    tu.color(details['color'])
    tu.end_fill()
    for step in details['layout']:
        if step[0] == 'fd':
            tu.fd(step[1])
        elif step[0] == 'rt':
            tu.rt(step[1])
        elif step[0] == 'fl':
            if step[1] == True:
                tu.begin_fill()
            else:
                tu.end_fill()
        elif step[0] == 'set':
            tu.up()
            tu.setx(step[1][0])
            tu.sety(step[1][1])
            tu.down()
        elif step[0] == 'sh':
            tu.setheading(step[1])

tu.up()
tu.done()
