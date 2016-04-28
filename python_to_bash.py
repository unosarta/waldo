import readit as r

filename = input('Please name the MCNP file to be made into VTK format: ')

readable = r.structure(filename)
vtk_contents = r.vtk_builder(readable)	


