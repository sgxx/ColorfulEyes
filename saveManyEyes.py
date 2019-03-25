#coding=utf-8

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time,matplotlib
from numpy import pi as pi
from math import radians as radians
from math import sqrt as sqrt
from math import cos as cos
from math import sin as sin
from math import tan as tan
from math import atan as atan
import math
from random import choice as choice
import random

#todo 用于生成很多的美瞳照片并且保存到目录中

if __name__ == '__main__':
    values = matplotlib.cm.cmap_d.keys()
    # values=["plasma"]
    length=2*len(values)

    count=0

    filepath=r'C:\Users\esa72\PycharmProjects\sgx\Date\201902\CoordTransfer\visualization\projection\image'

    a=6378137
    b=6356752.314

    u=np.linspace(0,2*pi,100)
    v=np.linspace(0,pi,100)

    x=a*np.outer(np.cos(u),np.sin(v))
    y=a*np.outer(np.sin(u),np.sin(v))
    z=b*np.outer(np.ones(np.size(u)),np.cos(v))

    for value in values:
        u0=pi/3
        v0=pi/3

        x0=a*cos(u0)*sin(v0)
        y0=a*sin(u0)*sin(v0)
        z0=b*cos(v0)

        fig=plt.figure()
        ax=fig.gca(projection='3d')

        plt.axis('off')

        i=0

        xs=[x0]
        ys=[y0]
        zs=[z0]

        for i in np.linspace(0,2*pi,100):
            x_yuanzhui=15000000*cos(radians(60))*sin(i)
            y_yuanzhui=15000000*cos(radians(60))*cos(i)
            z_yuanzhui=10000000-15000000*sin(radians(60))

            plt.plot([0, x_yuanzhui], [0, y_yuanzhui], [10000000, z_yuanzhui], color='black', linestyle='--')

        ax.scatter(xs,ys,zs,color='gray',s=20)

        ax.plot_surface(x,y,z,cmap=value,alpha=0.7)

        ax.set_xlim(-4500000,4500000)
        ax.set_ylim(-4500000,4500000)
        ax.set_zlim(-9000000,9000000)

        ax.view_init(90,0)

        plt.title(value)
        # plt.show()

        count += 1
        print(str(count) + "\\" + str(length), value)
        plt.savefig(filepath + "\\" + str(count) + ".png")

        ax.view_init(270, 0)

        count += 1
        print(str(count) + "\\" + str(length), value)
        plt.savefig(filepath + "\\" + str(count) + ".png")

        plt.title(value)
        # plt.show()

        # plt.close()

