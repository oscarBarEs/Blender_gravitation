from bmesh import new
import bpy
import random
from mathutils import *
import math
import numpy as np

#intrp=3

"""
   Delete moons
"""
print(bpy.context.active_object.name)
#localizacion cuepor estelar principal
loc_x=bpy.context.active_object.location[0]
loc_y=bpy.context.active_object.location[1]
loc_z=bpy.context.active_object.location[2]
#escala cuepor estelar principal (CEP)
#x_tam=bpy.context.active_object.scale[0]
#y_tam=bpy.context.active_object.scale[1]
#z_tam=bpy.context.active_object.scale[2]
#Tamaño cuepor estelar principal (CEP)
x_tam=bpy.context.active_object.dimensions[0]
y_tam=bpy.context.active_object.dimensions[1]
z_tam=bpy.context.active_object.dimensions[2]

bpy.ops.object.select_all(action='DESELECT')
    
for ob in bpy.context.scene.objects:
    if 'PEA' in ob.name:
        ob.select_set(True)
    
    bpy.ops.object.delete()
# Registramos el driver de posición
#bpy.app.driver_namespace['get_pos'] = get_pos


#Cada cuantos frames se inserta un keyframe (menos mayor precision pero mas calculo computacional)
masframe=24
#Proporcion entre CEP y lunas (num = veces mayor CEP)
"""Size of the moons"""
escala_min = 10
escala_max = 17
""""""
#angulo de desplazamiento entre cada frame
angulo_x = math.radians(20)


#Numero de lunas TOTAL
"""Number of moons"""
num_lunas = 15
'''''' 
for i in range (num_lunas):
    #Calculo radio de los ejes que conforman la elipsis orbital de las lunas
    """Size of the radios"""
    semieje_a = random.uniform(x_tam*1.2 , x_tam*1.9  )
    semieje_b = random.uniform(x_tam*0.2 , x_tam*0.8  )
    '''''' 
    #altura inicial de la luna
    h = random.uniform(0.5 ,y_tam*2 + 1.2)
    #creacion luna
    esca=random.uniform(x_tam/escala_max,x_tam/escala_min)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=7, ring_count=11,radius=1, enter_editmode=False, align='WORLD', location=(semieje_a , semieje_b , h ), scale=(esca, esca,esca))
    building = bpy.context.active_object
    building.name = 'PEA_moon_left' 

    #inicializacion valores
    frame_actual = 0
    angulo_actual_x = angulo_x + math.radians(random.randint(-90,90))
    #sentido de giro
    varia = random.randint(-1,1)
    #inclinacion eje z
    """Inclinacion """
    mod_z= random.uniform(0.0,1.3)
    '''''' 
    
    #variacion velocidad
    v =  math.radians(random.randint(0,50))
    for x in range (100):

        #Calculo elipsis
        ope1 = (math.cos(angulo_actual_x)**2)/((abs(semieje_a))**2)
        ope2 = (math.sin(angulo_actual_x)**2)/((abs(semieje_b))**2)
        
        x_actual = 0 + ((math.sqrt(ope1+ope2))**(-1))*math.cos(angulo_actual_x)
        y_actual = 0 + ((math.sqrt(ope1+ope2))**(-1))*math.sin(angulo_actual_x)

        #Asignacion valor calculado
        """Direction of the moons"""
        if (i < num_lunas/2 ):
            building.location = Vector((x_actual + loc_x ,y_actual + loc_y, x_actual*mod_z + loc_z))
        else: 
            building.location = Vector((x_actual + loc_x,y_actual + loc_y ,-x_actual*mod_z + loc_z))
        '''''' 
        building.keyframe_insert(data_path='location', frame = frame_actual)
        building.select_set(False)
        #asignacion Drivers
        # Valores siguiente frame
        frame_actual += masframe
        angulo_actual_x += angulo_x + v
        


