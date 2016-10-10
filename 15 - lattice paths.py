from math import factorial

gridw = 20
gridh = 20
gridsize = gridw*gridh

routes = (factorial(gridw+gridh))/(factorial((gridw+gridh)-gridh)*factorial(gridh))
print(routes)