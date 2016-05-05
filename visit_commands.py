import os.path
path_name = 'particle1.vtk'
i = 1
while os.path.exists(path_name):
	OpenDatabase(path_name)
	AddPlot('Mesh', 'mesh')
	DrawPlots()
	i += 1
	path_name = 'particle' + str(i) + '.vtk'
