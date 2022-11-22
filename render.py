import math
from turtle import width
from Obj import Obj
import random
from WriteUtilities import * 
from Color import *
from vector import V3
from textures import *
from matriz import *
from math import *
colors={'Body4': (0, 0, 1), 'Body5': (0.8, 0.8, 1), 'Body6': (0.8, 0.8, 1), 'Body11': (0.8, 0.8, 1), 'Body12': (0.8, 0.8, 1), 'Body13': (0.8, 0.8, 1), 'Body14': (0.8, 0.8, 1), 'Body15': (0.8, 0.8, 1), 'Body16': (0.8, 0.8, 1), 'Body17': (0.8, 0.8, 1), 'Body488': (0, 0, 1)}
colors={}

class Render(object):
    
    def __init__(self,w=None,h=None):
        print("Render Class Created")
        self.pointcolor(1,0,1)
        self.yVp=0
        self.xVp=0
        self.width=w
        self.height=h
        self.texture=None
        self.trianguloarray = []
        self.luz =V3(0,0,-1)
        self.Model = None
        self.Vista = None
        self.Projection = None
        self.ViewPort = None
        self.active_shader=None
        self.planetarray=[]
     
    def loadModelMatriz(self,translate=(0,0,0),scale=(1,1,1),rotate=(0,0,0)):
        translate=V3(*translate)
        scale=V3(*scale)
        rotate=V3(*rotate)
        
        translateM=MM([
            [1,0,0,translate.x],
            [0,1,0,translate.y],
            [0,0,1,translate.z],
            [0,0,0,1]
        ])
        
        scaleM=MM([
            [scale.x,      0,      0,0],
            [      0,scale.y,      0,0],
            [      0,      0,scale.z,0],
            [      0,      0,      0,1]
        ])
        a=rotate.x
        rotacionx=MM([
            [1,     0,           0, 0],
            [0, cos(a),    -sin(a), 0],
            [0, sin(a),     cos(a), 0],
            [0,     0,          0,  1]
        ])
        a=rotate.y
        rotaciony=MM([
            [ cos(a),     0,    sin(a), 0],
            [      0,     1,         0, 0],
            [-sin(a),     0,    cos(a), 0],
            [      0,     0,         0, 1]
        ])
        a=rotate.z
        rotacionz=MM([
            [cos(a),-sin(a),    0,0],
            [sin(a), cos(a),    0,0],
            [     0,      0,    1,0],
            [     0,      0,    0,1]
        ])
        rotacionM=rotacionx * rotaciony * rotacionz
        self.Model = translateM *rotacionM * scaleM
    
    def loadViewMatrix(self, x, y, z, center):
        Mi = MM([
            [x.x, x.y, x.z, 0],
            [y.x, y.y, y.z, 0],
            [z.x, z.y, z.z, 0], 
            [0,0,0,1]

        ])

        O = MM([
            [1, 0, 0, -center.x],
            [0, 1, 0, -center.y],
            [0, 0, 1, -center.z],
            [0, 0, 0,         1]
        ])

        self.Vista = Mi * O

    def loadProjectionMatrix(self):
        #coef = -1/(eye.length() -center.length())
        self.Projection = MM([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,-0.001,1],
            
        ])
        
    def loadVieportMatrix(self):
        
        x=0
        y=0
        w=self.width/2
        h=self.height/2
        
        self.ViewPort = MM([
            [w,0,   0,  x + w],
            [0,h,   0,  y + h],
            [0,0, 128,  128  ],
            [0,0,   0,  1    ],
            
        ])

    def lookAt(self, eye, center, up):
        eye = V3(*eye)
        center = V3(*center)
        up = V3(*up)

        z = (eye-center).normalize()
        x = (up * z).normalize()
        y = (z * x).normalize()

        #self.active_shader=self.shader
        self.loadViewMatrix(x,y,z, center)
        self.loadProjectionMatrix()
    
    def vertexConvert (self,x,y):
        return [round(self.xVp+(x+1)*0.5*self.widthVp-1),round(self.yVp+(y+1)*0.5*self.heightVp-1)]    
    
    def viewPort (self,x,y,neww,newh):
        self.widthVp = neww
        self.heightVp = newh
        self.yVp=y
        self.xVp=x
        self.loadVieportMatrix()
        
        
    def get_Texture(self,nombre):
        t=Texture(nombre)
        self.texture=t
    
    def backgroundcolor(self,r,g,b):
        self.color = [intcolor(r),intcolor(g),intcolor(b)]
    
    def pointcolor(self,r,g,b):
        #print("red:"+str(r)+" green: "+str(g)+" blue: "+str(b))
        self.pcolor =[intcolor(r),intcolor(g),intcolor(b)]
    
    def bufferStart (self, width, height):
        self.width = width
        self.height = height 
        self.heightVp =height
        self.widthVp =width
        
        self.backgroundcolor(0,0,0)
        self.clear()
        
    def clear (self):
        self.framebuffer=[
            [rgbcolor(*self.color) for x in range(self.width)]
            for y in range(self.height)
        ]
        
        self.zBuffer=[
            [-99999 for x in range(self.width)]
            for y in range(self.height)
        ]
        
        self.zpaint=[
            [rgbcolor(*(10,50,180)) for x in range(self.width)]
            for y in range(self.height)
        ]
        
    def write(self, filename="a.bmp"):
        f = open(filename, 'bw')
        
        extraBytes = (4 - (self.width * 3) % 4) % 4
        new_width_bytes = (self.width * 3) + extraBytes
        
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width_bytes * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
            extra = []
            for i in range(extraBytes):
                extra.append(0)
            f.write(bytes(extra))
        f.close()
        print("BMP Create in "+filename)
    
    def writez(self):
        f = open("zbuffer.bmp", 'bw')
        
        extraBytes = (4 - (self.width * 3) % 4) % 4
        new_width_bytes = (self.width * 3) + extraBytes
        
        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + new_width_bytes * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))
        
        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.height * self.width * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        
        #pixel data
        
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.zpaint[x][y])
            extra = []
            for i in range(extraBytes):
                extra.append(0)
            f.write(bytes(extra))
        f.close()
        
    def point(self, x,y):
        if (x < self.width and x >= 0 and y < self.height and y >= 0):
            self.framebuffer[y][x] = rgbcolor(*self.pcolor)
            
    def bounding_box(self,A,B,C):
        xs=[A.x,B.x,C.x]
        ys=[A.y,B.y,C.y]
        
        xs.sort()
        ys.sort()
        return V3(xs[0],ys[0]),V3(xs[-1],ys[-1])
    
    def baricentric(self,A,B,C,P):
        cx,cy,cz = V3.cross(
            V3(B.x - A.x,C.x - A.x,A.x - P.x),
            V3(B.y - A.y,C.y - A.y,A.y - P.y)
        )
        
        u= cx / cz
        v= cy / cz
        w= 1 -(cx + cy)/cz 
        return (w,u,v)
    
    def triangulo2(self,temp):
        #temp =[v1,v2,v3]
        for i in range(len(temp)):
            self.line(temp[i],temp[(i+1)%3])
    
    def shader(self,**kwargs):
                
        w,u,v = kwargs['bar']
        L=kwargs['light']
        v1,v2,v3 = kwargs['vertices']
        tA,tB,tC = kwargs['texture_coords']
        nA,nB,nC = kwargs['normals']
        
        iA=nA.normalize() @ L.normalize()
        iB=nB.normalize() @ L.normalize()
        iC=nC.normalize() @ L.normalize()
        i = (iA * w + iB * u + iC * v)*1.75

        
        
        if self.texture:
            tx = tA.x * w + tB.x * u + tC.x * v
            ty = tA.y * w + tB.y * u + tC.y * v 
            return self.texture.intensity(tx, ty, -i)
        else:
            return (round(self.pcolor[0]*-i),round(self.pcolor[1]*-i),round(self.pcolor[2]*-i))

    def planeta(self,**kwargs):
                    
        w,u,v = kwargs['bar']
        L=kwargs['light']
        v1,v2,v3 = kwargs['vertices']
        tA,tB,tC = kwargs['texture_coords']
        nA,nB,nC = kwargs['normals']
        x= kwargs['coordX']
        y= kwargs['coordY']

        
        iA=nA.normalize() @ L.normalize()
        iB=nB.normalize() @ L.normalize()
        iC=nC.normalize() @ L.normalize()
        i = (iA * w + iB * u + iC * v)*-1.75

        self.pcolor=(round(122*i),round(122*i),round(122*i))
        self.point(round((x/4)+25),round((y/4)))

        self.pcolor=(round(218*i),round(218*i),round(218*i))
        self.point(round((x/4.5)+self.width*0.7),round((y/4.5)+self.width*0.7))

        rojorandom= random.randint(0,50)
        rojo = 238 +rojorandom
        verde = 109
        azul= 60
        aleatorio = random.randint(0,3)
        
        if y % 2 ==0:
            if x >355 and aleatorio ==2:
                return (round(245*i),round(120*i),round(66*i))
            elif aleatorio== 1:
                return (round(234*i),round(105*i),round(56*i))
            else:
                return (round(rojo*i),round(verde*i),round(azul*i))

        else:
            if x <355 and aleatorio ==3:
                return (round(245*i),round(120*i),round(66*i))
            elif aleatorio== 3:
                return (round(234*i),round(105*i),round(56*i))
            else:
                return (round(rojo*i),round(verde*i),round(azul*i))

    def triangulo(self):
        
        #v1,v2,v3=Vertices
        v1=next(self.trianguloarray)
        v2=next(self.trianguloarray)
        v3=next(self.trianguloarray)
        
        tA=next(self.trianguloarray)
        tB=next(self.trianguloarray)
        tC=next(self.trianguloarray)
            #tA,tB,tC=Tvertices
        
        nA=next(self.trianguloarray)
        nB=next(self.trianguloarray)
        nC=next(self.trianguloarray)

        
        #Quitar
        L=self.luz
        N = (v3-v1) * (v2-v1)
        
        
        i= N.normalize() @ L.normalize()
        
        if i <= 0 or i>1:
            return
        
        #Quitar
        
        Bmin,Bmax = self.bounding_box(v1,v2,v3)
        Bmin.round()
        Bmax.round()
        
        for x in range(Bmin.x,Bmax.x+1):
            for y in range(Bmin.y,Bmax.y+1):
                w,u,v = self.baricentric(v1,v2,v3,V3(x,y))
                
                if(w<0 or v<0 or u <0):
                    continue
                
                z= v1.z * w + v2.z * v + v3.z * u
                if (self.zBuffer[x][y]<z):
                    self.zBuffer[x][y]=z
                    """
                    if self.texture:
                        tx = tA.x * w + tB.x * u + tC.x * v
                        ty = tA.y * w + tB.y * u + tC.y * v 
                        self.pcolor = self.texture.intensity(tx, ty, i)
                    """
                    #"""
                    if self.texture:
                        self.pcolor=self.shader(

                            bar=(w,u,v),
                            vertices=(v1,v2,v3),
                            texture_coords = (tA,tB,tC),
                            normals=(nA,nB,nC),
                            light= self.luz,
                        )
                    else:
                        #Borrrar entrega planeta
                        self.pcolor=self.planeta(

                            bar=(w,u,v),
                            vertices=(v1,v2,v3),
                            texture_coords = (tA,tB,tC),
                            normals=(nA,nB,nC),
                            light= self.luz,
                            coordX=x,
                            coordY=y

                        )
                    #"""
                    
                    
                    self.point(x,y)
        pass
        
    def clamp(self,val):
        temp= round(val*255)
        return max(0,min(temp,255))
        
    def line (self,V1,V2):
        x0=V1.x
        y0=V1.y
        x1=V2.x
        y1=V2.y   
        dy = abs(y1 -y0)
        dx = abs(x1- x0)
        steep = dy > dx    
        
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        if x0>x1:
            x0,x1 = x1,x0
            y0,y1 = y1,y0
        
        dy = abs(y1 -y0)
        dx = abs(x1- x0)
        
        offset=0
        threshold = dx * 2
        y=y0
        for x in range(x0,x1+1):
            if steep:
                self.point(y,x)
                ##self.point(y,x+1)
                ##self.point(y-1,x)
                ##self.point(y-1,x+1)
                
                
                
                
                
            else:
                self.point(x,y)
                #self.point(x+1,y)
                #self.point(x,y-1)
                #self.point(x+1,y-1)
                
                
                
            offset+=dy*2
            if offset >= threshold:
                y+=1 if y0<y1 else -1
                threshold+=dx*2

    def transform_vertex(self,vertex):
        
        vertex_aumentado=MM([[vertex[0]],[vertex[1]],[vertex[2]],[1]])
        transformed_vertex= self.ViewPort * self.Projection * self.Vista * self.Model * vertex_aumentado
        
        
        return V3(
            transformed_vertex.matriz[0][0]/transformed_vertex.matriz[3][0],
            transformed_vertex.matriz[1][0]/transformed_vertex.matriz[3][0],
            transformed_vertex.matriz[2][0]/transformed_vertex.matriz[3][0]
            
        )
    def fondo(self,nombre):
        t=Texture(nombre)
        self.framebuffer=t.pixels

    def plano(self,nombre,OBJ3D):
        t=Texture(nombre)
        self.framebuffer=t.pixels


        figura = Obj(OBJ3D+'.obj')
        w=[t.width,t.heigth,0]
        e=[0,0,0]


        for face in figura.caras:
            g=face.pop()
            if len(face)==3:
                f1 = face[0][1] - 1
                f2 = face[1][1] - 1
                f3 = face[2][1] - 1

                v1 = self.transform_vertex(figura.tvertices[f1],w,e)
                v2 = self.transform_vertex(figura.tvertices[f2],w,e)
                v3 = self.transform_vertex(figura.tvertices[f3],w,e)

                self.triangulo2((v1,v2,v3))
            
            if len(face)==4:
                
                f1 = face[0][1] - 1
                f2 = face[1][1] - 1
                f3 = face[2][1] - 1
                f4 = face[3][1] - 1

                v1 = self.transform_vertex(figura.tvertices[f1],w,e)
                v2 = self.transform_vertex(figura.tvertices[f2],w,e)
                v3 = self.transform_vertex(figura.tvertices[f3],w,e)
                v4 = self.transform_vertex(figura.tvertices[f4],w,e)

                
                self.triangulo2((v1,v2,v3))
                self.triangulo2((v1,v3,v4))
                
                
        self.write()   
    
    def ObjCall(self,nombre,color):
            figura = Obj(nombre+'.obj')
            self.pointcolor(*color)
            for face in figura.caras:
                if len(face)==4:
                    f1 = face[0][0] - 1
                    f2 = face[1][0] - 1
                    f3 = face[2][0] - 1
                    f4 = face[3][0] - 1

                    v1 = self.transform_vertex(figura.vertices[f1])
                    v2 = self.transform_vertex(figura.vertices[f2])
                    v3 = self.transform_vertex(figura.vertices[f3])
                    v4 = self.transform_vertex(figura.vertices[f4])


                   
                    #Si truena
                    
                    try:
                    
                        fn1 = face[0][2] - 1
                        fn2 = face[1][2] - 1
                        fn3 = face[2][2] - 1
                        fn4 = face[3][2] - 1
                        
                        
                        vn1 = self.transform_vertex(figura.nvertices[fn1])
                        vn2 = self.transform_vertex(figura.nvertices[fn2])
                        vn3 = self.transform_vertex(figura.nvertices[fn3])
                        vn4 = self.transform_vertex(figura.nvertices[fn4])

                    except:
                        vn1 = 0
                        vn2 = 0
                        vn3 = 0
                        vn4 = 0
                    
                    try:
                        ft1 = face[0][1] - 1
                        ft2 = face[1][1] - 1
                        ft3 = face[2][1] - 1
                        ft4 = face[3][1] - 1

                        vt1 = V3(*figura.tvertices[ft1])
                        vt2 = V3(*figura.tvertices[ft2])
                        vt3 = V3(*figura.tvertices[ft3])
                        vt4 = V3(*figura.tvertices[ft4])
                    except:
                        vt1=0
                        vt2=0
                        vt3=0
                        vt4=0
                        

                    #self.trianguloarray.extend(v1,v2,v3,vt1,vt2,vt3)
                    self.trianguloarray.append(v1)
                    self.trianguloarray.append(v2)
                    self.trianguloarray.append(v3)
                    self.trianguloarray.append(vt1)
                    self.trianguloarray.append(vt2)
                    self.trianguloarray.append(vt3)
                    self.trianguloarray.append(vn1)
                    self.trianguloarray.append(vn2)
                    self.trianguloarray.append(vn3)
                    
                    
                    self.trianguloarray.append(v1)
                    self.trianguloarray.append(v3)
                    self.trianguloarray.append(v4)
                    self.trianguloarray.append(vt1)
                    self.trianguloarray.append(vt3)
                    self.trianguloarray.append(vt4)
                    self.trianguloarray.append(vn1)
                    self.trianguloarray.append(vn3)
                    self.trianguloarray.append(vn4)
                
                if len(face)==3:
                    f1 = face[0][0] - 1
                    f2 = face[1][0] - 1
                    f3 = face[2][0] - 1

                    v1 = self.transform_vertex(figura.vertices[f1])
                    v2 = self.transform_vertex(figura.vertices[f2])
                    v3 = self.transform_vertex(figura.vertices[f3])



                    try:
                    
                        fn1 = face[0][2] - 1
                        fn2 = face[1][2] - 1
                        fn3 = face[2][2] - 1
                        
                        
                        vn1 = self.transform_vertex(figura.nvertices[fn1])
                        vn2 = self.transform_vertex(figura.nvertices[fn2])
                        vn3 = self.transform_vertex(figura.nvertices[fn3])

                    except:
                        vn1 = 0
                        vn2 = 0
                        vn3 = 0
                    
                    try:
                        ft1 = face[0][1] - 1
                        ft2 = face[1][1] - 1
                        ft3 = face[2][1] - 1
                        vt1 = V3(*figura.tvertices[ft1])
                        vt2 = V3(*figura.tvertices[ft2])
                        vt3 = V3(*figura.tvertices[ft3])
                    except:
                        vt1 = 0
                        vt2 = 0
                        vt3 = 0
                        
                    
                    self.trianguloarray.append(v1)
                    self.trianguloarray.append(v2)
                    self.trianguloarray.append(v3)
                    self.trianguloarray.append(vt1)
                    self.trianguloarray.append(vt2)
                    self.trianguloarray.append(vt3)
                    self.trianguloarray.append(vn1)
                    self.trianguloarray.append(vn2)
                    self.trianguloarray.append(vn3)

            self.draw()


    #Borrar entrega planeta
    def manchas(self):
    
        desplazamientoY=round(self.height*0.30)
        desplazamientoX=round(self.width*0.45)


        for y in range(100):
            xx= random.uniform(0.8,1)
            for x in range(40):
                eleccion= random.randint(0,2)

                i=((y+desplazamientoY)/self.height)*1.75

                if eleccion == 1:
                    #self.pcolor=(round(65*i),round(45*i),round(43*i))
                    self.pcolor=(round(245*i),round(120*i),round(66*i))
                    self.point(x+round((desplazamientoX-y)*xx),y+(desplazamientoY))
                    i=((y-10+(desplazamientoY))/self.height)*1.75
                    self.pcolor=(round(245*i),round(120*i),round(66*i))
                    self.point(x+round((desplazamientoX+y)*xx),y-10+(desplazamientoY))
                    i=((y-50+(desplazamientoY))/self.height)*1.75
                    self.pcolor=(round(245*i),round(120*i),round(66*i))
                    self.point(x+round((desplazamientoX-y)*xx),y-50+(desplazamientoY))


                elif eleccion == 2:
                    #self.pcolor=(round(97*i),round(58*i),round(50*i))
                    self.pcolor=(round(234*i),round(105*i),round(56*i))
                    self.point(x+round((desplazamientoX-y)*xx),y+(desplazamientoY))
                    i=((y-10+(desplazamientoY))/self.height)*1.75
                    self.pcolor=(round(234*i),round(105*i),round(56*i))
                    self.point(x+round((desplazamientoX+y)*xx),y-10+(desplazamientoY))
                    i=((y-50+(desplazamientoY))/self.height)*1.75
                    self.pcolor=(round(234*i),round(105*i),round(56*i))
                    self.point(x+round((desplazamientoX-y)*xx),y-50+(desplazamientoY))

                else:
                    self.pcolor=(round(250*i),round(124*i),round(73*i))
                    self.point(x+round((desplazamientoX-y)*xx),y+(desplazamientoY))
                    i=((y-10+(desplazamientoY))/self.height)*1.75
                    self.pcolor=(round(250*i),round(124*i),round(73*i))
                    self.point(x+round((desplazamientoX+y)*xx),y-10+(desplazamientoY))
                    i=((y-50+(desplazamientoY))/self.height)*1.75
                    self.pcolor=(round(250*i),round(124*i),round(73*i))
                    self.point(x+round((desplazamientoX-y)*xx),y-50+(desplazamientoY))
                



        desplazamientoY=round(self.height*0.66)
        desplazamientoX=round(self.width*0.75)


        for y in range(90):
            xx= random.uniform(0.65,0.9)
            for x in range(50):
                eleccion= random.randint(0,2)

                if eleccion == 1:
                    self.pcolor=(round(105),round(49),round(27))

                
                elif eleccion == 2:
                    self.pcolor=(round(105),round(49),round(27))

                else:
                    self.pcolor=(round(105),round(49),round(27))

                self.point(x+round((desplazamientoX-y)*xx),y+(desplazamientoY))
                self.point(x+round((desplazamientoX-y)*xx),y-50+(desplazamientoY))
                self.point(x-35+round((desplazamientoX-y)*xx),-y+(desplazamientoY))


        desplazamientoY=round(self.height*0.45)
        desplazamientoX=round(self.width*0.84)


        for y in range(35):
            xx= random.uniform(0.65,0.9)
            for x in range(47):
                eleccion= random.randint(0,2)

                if eleccion == 1:
                    self.pcolor=(round(105),round(49),round(27))

                
                elif eleccion == 2:
                    self.pcolor=(round(105),round(49),round(27))

                else:
                    self.pcolor=(round(105),round(49),round(27))

                self.point(x+round((desplazamientoX-y)*xx),y+(desplazamientoY))
                self.point(x+round((desplazamientoX-y)*xx),y-15+(desplazamientoY))
                self.point(x-20+round((desplazamientoX-y)*xx),y-55+(desplazamientoY))

        
        desplazamientoY=round(self.height*0.5)
        desplazamientoX=round(self.width*0.32)


        for y in range(35):
            xx= random.uniform(0.65,0.9)
            for x in range(20):
                eleccion= random.randint(0,2)

                if eleccion == 1:
                    self.pcolor=(round(105),round(49),round(27))

                
                elif eleccion == 2:
                    self.pcolor=(round(105),round(49),round(27))

                else:
                    self.pcolor=(round(105),round(49),round(27))

                self.point(x+round((desplazamientoX-y)*xx),y+(desplazamientoY))
                self.point(x+20+round((desplazamientoX-y)*xx),y+35+(desplazamientoY))
                self.point(x+20+round((desplazamientoX-y)*xx),y-35+(desplazamientoY))


            
    def draw (self):
        self.trianguloarray=iter(self.trianguloarray)
        try:
            while True:
                self.triangulo()
        except: StopIteration
        self.manchas()

    
                    
        