"""
Setting illumination properties:
ambient, diffuse
specular, specularPower, specularColor.
"""
#https://lorensen.github.io/VTKExamples/site/Python/Rendering/SpecularSpheres
from vtkplotter import Plotter, Text, Arrow, datadir


vp = Plotter(axes=8, bg="w")

ambient, diffuse, specular = 0.1, 0., 0.
specularPower, specularColor= 20, 'white'

for i in range(8):
    s = vp.load(datadir+'pumpkin.vtk')#.color(i)
    s.normalize().pos((i%4)*2.2, int(i<4)*3, 0)
    
    #s.phong()
    #s.gouraud()
    s.flat()
    
    # modify the default with specific values
    s.lighting('default', ambient, diffuse, specular, specularPower, specularColor)
    #ambient += 0.125
    diffuse += 0.125
    specular += 0.125
    
vp.add(Text(__doc__))
vp.show()

print('Adding a light source..')
p = (3, 1.5, 3)
f = (3, 1.5, 0)
vp.addLight(pos=p, focalPoint=f)
vp.add(Arrow(p,f, s=0.01, c='gray', alpha=0.2))
vp.show()
