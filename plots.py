#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:29:25 2022

@author: charliestamp
"""

import numpy as np

from sympy import Point3D, Plane
import matplotlib.pyplot as plt

import ray as r
import OpticalElement as oe

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=400, z2=400, z0=100, z01=360,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

r1 = r.ray([0, 0, 0], [0.1, 0, 1])
r2 = r.ray([0, 0, 0], [0.075, 0, 1])
r3 = r.ray([0, 0, 0], [0.05, 0, 1])
r4 = r.ray([0, 0, 0], [0.025, 0, 1])
r5 = r.ray([0, 0, 0], [0, 0, 1])
r6 = r.ray([0, 0, 0], [-0.025, 0, 1])
r7 = r.ray([0, 0, 0], [-0.05, 0, 1])
r8 = r.ray([0, 0, 0], [-0.075, 0, 1])
r8 = r.ray([0, 0, 0], [-0.1, 0, 1])
r9 = r.ray([0, 0, 0], [2.5, 0, 10])
r10 = r.ray([0, 0, 0], [-2.5, 0, 10])

l.intercept(r1)
l.snells(r1)
l.propagate_ray(r1)
os.first_plane_intercept(r1)
os.first_plane_point(r1)

l.intercept(r2)
l.snells(r2)
l.propagate_ray(r2)
os.first_plane_intercept(r2)
os.first_plane_point(r2)

l.intercept(r3)
l.snells(r3)
l.propagate_ray(r3)
os.first_plane_intercept(r3)
os.first_plane_point(r3)

l.intercept(r4)
l.snells(r4)
l.propagate_ray(r4)
os.first_plane_intercept(r4)
os.first_plane_point(r4)

l.intercept(r5)
l.snells(r5)
l.propagate_ray(r5)
os.first_plane_intercept(r5)
os.first_plane_point(r5)

l.intercept(r6)
l.snells(r6)
l.propagate_ray(r6)
os.first_plane_intercept(r6)
os.first_plane_point(r6)

l.intercept(r7)
l.snells(r7)
l.propagate_ray(r7)
os.first_plane_intercept(r7)
os.first_plane_point(r7)

l.intercept(r8)
l.snells(r8)
l.propagate_ray(r8)
os.first_plane_intercept(r8)
os.first_plane_point(r8)

l.intercept(r9)
l.snells(r9)
l.propagate_ray(r9)
os.first_plane_intercept(r9)
os.first_plane_point(r9)

l.intercept(r10)
l.snells(r10)
l.propagate_ray(r10)
os.first_plane_intercept(r10)
os.first_plane_point(r10)

plt.plot(np.array(r1.vertices())[:, 2], np.array(r1.vertices())[:, 0])
plt.plot(np.array(r2.vertices())[:, 2], np.array(r2.vertices())[:, 0])
plt.plot(np.array(r3.vertices())[:, 2], np.array(r3.vertices())[:, 0])
plt.plot(np.array(r4.vertices())[:, 2], np.array(r4.vertices())[:, 0])
plt.plot(np.array(r5.vertices())[:, 2], np.array(r5.vertices())[:, 0])
plt.plot(np.array(r6.vertices())[:, 2], np.array(r6.vertices())[:, 0])
plt.plot(np.array(r7.vertices())[:, 2], np.array(r7.vertices())[:, 0])
plt.plot(np.array(r8.vertices())[:, 2], np.array(r8.vertices())[:, 0])
plt.plot(np.array(r9.vertices())[:, 2], np.array(r9.vertices())[:, 0])
plt.plot(np.array(r10.vertices())[:, 2], np.array(r10.vertices())[:, 0])
plt.grid()
plt.title("")
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
# plt.xlim(195,205)
plt.title("Paraxial vs marginal rays")
plt.style.use('dark_background')
plt.show()

# %%

# Task 10

a = r.ray([0.1, 0, 0], [0, 0, 1])
# print(a)
b = r.ray([0.075, 0, 0], [0, 0, 1])
c = r.ray([0.05, 0, 0], [0, 0, 1])
d = r.ray([0.025, 0, 0], [0, 0, 1])
e = r.ray([0, 0, 0], [0, 0, 1])
f = r.ray([-0.025, 0, 0], [0, 0, 1])
g = r.ray([-0.05, 0, 0], [0, 0, 1])
h = r.ray([-0.075, 0, 0], [0, 0, 1])
i = r.ray([-0.1, 0, 0], [0, 0, 1])

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=250, z2=300, z0=100, z01=250,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

l.intercept(a)
l.snells(a)
l.propagate_ray(a)
os.first_plane_intercept(a)
os.first_plane_point(a)

l.intercept(b)
l.snells(b)
l.propagate_ray(b)
os.first_plane_intercept(b)
os.first_plane_point(b)

l.intercept(c)
l.snells(c)
l.propagate_ray(c)
os.first_plane_intercept(c)
os.first_plane_point(c)

l.intercept(d)
l.snells(d)
l.propagate_ray(d)
os.first_plane_intercept(d)
os.first_plane_point(d)

l.intercept(e)
l.snells(e)
l.propagate_ray(e)
os.first_plane_intercept(e)
os.first_plane_point(e)

l.intercept(f)
l.snells(f)
l.propagate_ray(f)
os.first_plane_intercept(f)
os.first_plane_point(f)

l.intercept(g)
l.snells(g)
l.propagate_ray(g)
os.first_plane_intercept(g)
os.first_plane_point(g)

l.intercept(h)
l.snells(h)
l.propagate_ray(h)
os.first_plane_intercept(h)
os.first_plane_point(h)

l.intercept(i)
l.snells(i)
l.propagate_ray(i)
os.first_plane_intercept(i)
os.first_plane_point(i)

# print(a.vertices())
#print(np.array(a.vertices())[:, 2])
#print(a.vertices())[:, 0]


plt.plot(np.array(a.vertices())[:, 2], np.array(a.vertices())[:, 0])
plt.plot(np.array(b.vertices())[:, 2], np.array(b.vertices())[:, 0])
plt.plot(np.array(c.vertices())[:, 2], np.array(c.vertices())[:, 0])
plt.plot(np.array(d.vertices())[:, 2], np.array(d.vertices())[:, 0])
plt.plot(np.array(e.vertices())[:, 2], np.array(e.vertices())[:, 0])
plt.plot(np.array(f.vertices())[:, 2], np.array(f.vertices())[:, 0])
plt.plot(np.array(g.vertices())[:, 2], np.array(g.vertices())[:, 0])
plt.plot(np.array(h.vertices())[:, 2], np.array(h.vertices())[:, 0])
plt.plot(np.array(i.vertices())[:, 2], np.array(i.vertices())[:, 0])
plt.legend()
plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
# plt.xlim(195,205)
plt.title("Estimating the position of the paraxial focus")
plt.style.use('dark_background')
plt.show()

# %%

# Task 10

a = r.ray([0.1, 0, 0], [0, 0, 1])
# print(a)
b = r.ray([0.075, 0, 0], [0, 0, 1])
c = r.ray([0.05, 0, 0], [0, 0, 1])
d = r.ray([0.025, 0, 0], [0, 0, 1])
e = r.ray([0, 0, 0], [0, 0, 1])
f = r.ray([-0.025, 0, 0], [0, 0, 1])
g = r.ray([-0.05, 0, 0], [0, 0, 1])
h = r.ray([-0.075, 0, 0], [0, 0, 1])
i = r.ray([-0.1, 0, 0], [0, 0, 1])

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=250, z2=300, z0=100, z01=250,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

l.intercept(a)
l.snells(a)
l.propagate_ray(a)
os.first_plane_intercept(a)
os.first_plane_point(a)

l.intercept(b)
l.snells(b)
l.propagate_ray(b)
os.first_plane_intercept(b)
os.first_plane_point(b)

l.intercept(c)
l.snells(c)
l.propagate_ray(c)
os.first_plane_intercept(c)
os.first_plane_point(c)

l.intercept(d)
l.snells(d)
l.propagate_ray(d)
os.first_plane_intercept(d)
os.first_plane_point(d)

l.intercept(e)
l.snells(e)
l.propagate_ray(e)
os.first_plane_intercept(e)
os.first_plane_point(e)

l.intercept(f)
l.snells(f)
l.propagate_ray(f)
os.first_plane_intercept(f)
os.first_plane_point(f)

l.intercept(g)
l.snells(g)
l.propagate_ray(g)
os.first_plane_intercept(g)
os.first_plane_point(g)

l.intercept(h)
l.snells(h)
l.propagate_ray(h)
os.first_plane_intercept(h)
os.first_plane_point(h)

l.intercept(i)
l.snells(i)
l.propagate_ray(i)
os.first_plane_intercept(i)
os.first_plane_point(i)

plt.plot(np.array(a.vertices())[:, 2], np.array(a.vertices())[:, 0])
plt.plot(np.array(b.vertices())[:, 2], np.array(b.vertices())[:, 0])
plt.plot(np.array(c.vertices())[:, 2], np.array(c.vertices())[:, 0])
plt.plot(np.array(d.vertices())[:, 2], np.array(d.vertices())[:, 0])
plt.plot(np.array(e.vertices())[:, 2], np.array(e.vertices())[:, 0])
plt.plot(np.array(f.vertices())[:, 2], np.array(f.vertices())[:, 0])
plt.plot(np.array(g.vertices())[:, 2], np.array(g.vertices())[:, 0])
plt.plot(np.array(h.vertices())[:, 2], np.array(h.vertices())[:, 0])
plt.plot(np.array(i.vertices())[:, 2], np.array(i.vertices())[:, 0])
plt.legend()
plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.xlim(195, 205)
plt.title("Estimating the position of the paraxial focus")
plt.style.use('dark_background')
plt.show()

# %%

# Tracing a large-diameter uniform bundle of collimated rays through a spherical surface.

bund2 = r.bundle(r.ray, radius=[0, 2, 4, 6, 8, 10], num=[
                 1, 20, 40, 60, 80, 100])
bund2.circle_points(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])
bund2.circle_3dpoints(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])
bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[
                       1, 20, 40, 60, 80, 100])
print(bund2.propogate_circle(
    radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100]))

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=250, z2=300, z0=100, z01=250,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    l.intercept(i)
    l.snells(i)
    l.propagate_ray(i)
    os.first_plane_intercept(i)
    os.first_plane_point(i)

    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [A[0:, 2], B[0:, 2], C[0:, 2]]

    plt.plot(z_values, x_values, linestyle="-")

plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.title(
    "Large-diameter uniform bundle of collimated rays through a spherical surface")
plt.show()

# %%
l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=200, z2=300, z0=100, z01=200,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

disttotal = []

for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    l.intercept(i)
    l.snells(i)
    l.propagate_ray(i)
    os.first_plane_intercept(i)
    os.first_plane_point(i)

    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [A[0:, 2], B[0:, 2], C[0:, 2]]

    plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)

plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Corresponding spot diagram")
plt.show()

rms_total = np.sqrt(disttotal[-1]/301)
print(rms_total)


# %%
# Paraxial ray zx plot

bund1 = r.bundle(r.ray, radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                 1, 20, 40, 60, 80, 100])
bund1.circle_points(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                    1, 20, 40, 60, 80, 100])
bund1.circle_3dpoints(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                      1, 20, 40, 60, 80, 100])
bund1.propogate_circle(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                       1, 20, 40, 60, 80, 100])
print(bund1.propogate_circle(
    radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[1, 20, 40, 60, 80, 100]))

plt.scatter(np.array(bund1.circle_points(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[1, 20, 40, 60, 80, 100]))[
            :, 0], np.array(bund1.circle_points(radius=[0, 1, 2, 3, 4, 5], num=[1, 20, 40, 60, 80, 100]))[:, 1])
plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("The starting positions of the rays at z = 0")
plt.show()
sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=250, z0=5, z01=100,
                     curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

disttotal = []

for index, i in enumerate(bund1.propogate_circle(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[1, 20, 40, 60, 80, 100])):

    sr2.plane_snells_intercept(i)
    sr2.plane_snells(i)
    os2.first_plane_intercept(i)
    os2.first_plane_point(i)
    sr2.intercept(i)
    sr2.snells(i)
    sr2.propagate_ray(i)
    os2.second_plane_intercept(i)
    os2.second_plane_point(i)
    D = np.array([i.vertices()[-4]])
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [D[0:, 0], A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [D[0:, 2], A[0:, 2], B[0:, 2], C[0:, 2]]

    # print(y_values)
    #plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    plt.plot(z_values, x_values, linestyle="-")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)
    # print(rms)

plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.title("Paraxial ray plot: plane surface first")
plt.show()
# print(disttotal)

rms_total = np.sqrt(disttotal[-1]/301)
# print(rms_total)

# %%

# Paraxial ray focal plane plot

bund1 = r.bundle(r.ray, radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                 1, 20, 40, 60, 80, 100])
bund1.circle_points(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                    1, 20, 40, 60, 80, 100])
bund1.circle_3dpoints(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                      1, 20, 40, 60, 80, 100])
bund1.propogate_circle(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[
                       1, 20, 40, 60, 80, 100])
print(bund1.propogate_circle(
    radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[1, 20, 40, 60, 80, 100]))

plt.scatter(np.array(bund1.circle_points(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[1, 20, 40, 60, 80, 100]))[
            :, 0], np.array(bund1.circle_points(radius=[0, 1, 2, 3, 4, 5], num=[1, 20, 40, 60, 80, 100]))[:, 1])
plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("The starting positions of the rays at z = 0")
plt.show()
sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=199.249226, z0=5,
                     z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

disttotal = []

for index, i in enumerate(bund1.propogate_circle(radius=[0, 0.02, 0.04, 0.06, 0.08, 0.1], num=[1, 20, 40, 60, 80, 100])):

    sr2.plane_snells_intercept(i)
    sr2.plane_snells(i)
    os2.first_plane_intercept(i)
    os2.first_plane_point(i)
    sr2.intercept(i)
    sr2.snells(i)
    sr2.propagate_ray(i)
    os2.second_plane_intercept(i)
    os2.second_plane_point(i)
    D = np.array([i.vertices()[-4]])
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [D[0:, 0], A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [D[0:, 2], A[0:, 2], B[0:, 2], C[0:, 2]]

    # print(y_values)
    plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    #plt.plot(z_values,x_values, linestyle = "-")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)
    # print(rms)

plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Spot diagram of paraxial rays")
plt.show()
# print(disttotal)

rms_total = np.sqrt(disttotal[-1]/301)
print(rms_total)

# %%
# Plano-convex lens: plane surface first (zx plot)

bund2 = r.bundle(r.ray, radius=[0, 2, 4, 6, 8, 10], num=[
                 1, 20, 40, 60, 80, 100])
bund2.circle_points(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])
bund2.circle_3dpoints(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])
bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[
                       1, 20, 40, 60, 80, 100])
print(bund2.propogate_circle(
    radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100]))

plt.scatter(np.array(bund2.circle_points(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100]))[
            :, 0], np.array(bund2.circle_points(radius=[0, 1, 2, 3, 4, 5], num=[1, 20, 40, 60, 80, 100]))[:, 1])
plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("The starting positions of the rays at z = 0")
plt.show()

sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=250, z0=5, z01=100,
                     curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

disttotal = []

for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr2.plane_snells_intercept(i)
    sr2.plane_snells(i)
    os2.first_plane_intercept(i)
    os2.first_plane_point(i)
    sr2.intercept(i)
    sr2.snells(i)
    sr2.propagate_ray(i)
    os2.second_plane_intercept(i)
    os2.second_plane_point(i)
    D = np.array([i.vertices()[-4]])
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [D[0:, 0], A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [D[0:, 2], A[0:, 2], B[0:, 2], C[0:, 2]]

    # print(y_values)
    #plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    plt.plot(z_values, x_values, linestyle="-")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)
    # print(rms)

plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.title("Plano-convex lens: plane surface first")
plt.show()
# print(disttotal)

rms_total = np.sqrt(disttotal[-1]/301)
# print(rms_total)

# %%

# Plano-convex lens: plane surface first (focal plane plot)

bund2 = r.bundle(r.ray, radius=[0, 2, 4, 6, 8, 10], num=[
                 1, 20, 40, 60, 80, 100])
bund2.circle_points(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])
bund2.circle_3dpoints(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])
bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[
                       1, 20, 40, 60, 80, 100])
print(bund2.propogate_circle(
    radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100]))

plt.scatter(np.array(bund2.circle_points(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100]))[
            :, 0], np.array(bund2.circle_points(radius=[0, 1, 2, 3, 4, 5], num=[1, 20, 40, 60, 80, 100]))[:, 1])
plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("The starting positions of the rays at z = 0")
plt.show()
sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=199.249226, z0=5,
                     z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

disttotal = []

for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr2.plane_snells_intercept(i)
    sr2.plane_snells(i)
    os2.first_plane_intercept(i)
    os2.first_plane_point(i)
    sr2.intercept(i)
    sr2.snells(i)
    sr2.propagate_ray(i)
    os2.second_plane_intercept(i)
    os2.second_plane_point(i)
    D = np.array([i.vertices()[-4]])
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [D[0:, 0], A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [D[0:, 2], A[0:, 2], B[0:, 2], C[0:, 2]]

    # print(y_values)
    plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    #plt.plot(z_values,x_values, linestyle = "-")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)
    # print(rms)

plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Spot diagram: plane surface first")
plt.show()
# print(disttotal)

rms_total = np.sqrt(disttotal[-1]/301)
print(rms_total)

# %%

# Plano-convex lens: curved surface first (zx plot)

sr1 = oe.SphericalRefraction(
    z0=100, z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)
os1 = oe.OutputPlane(r.ray, z1=105, z2=250, z0=100, z01=105,
                     curvature=0.02, n1=1, n2=1.5168, a_radius=30)

disttotal1 = []
for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr1.intercept(i)
    sr1.plane_snells_intercept(i)
    sr1.plane_snells(i)
    os1.first_plane_intercept(i)
    os1.first_plane_point(i)
    os1.second_plane_intercept(i)
    os1.second_plane_point(i)
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])
    x_values = [A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [A[0:, 2], B[0:, 2], C[0:, 2]]
    #plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    plt.plot(z_values, x_values, linestyle="-")

    rms1 = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal1 = np.array(disttotal1+rms1)
    # print(rms)

plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.title("Plano-convex lens: spherical surface first")
plt.show()
# print(disttotal)

rms_total1 = np.sqrt(disttotal1[-1]/301)
# print(rms_total1)

# %%

# Plano-convex lens: curved surface first (focal plane plot)

sr1 = oe.SphericalRefraction(
    z0=100, z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)
os1 = oe.OutputPlane(r.ray, z1=105, z2=199.249226, z0=100,
                     z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)

disttotal1 = []
for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr1.intercept(i)
    sr1.plane_snells_intercept(i)
    sr1.plane_snells(i)
    os1.first_plane_intercept(i)
    os1.first_plane_point(i)
    os1.second_plane_intercept(i)
    os1.second_plane_point(i)
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])
    x_values = [A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [A[0:, 2], B[0:, 2], C[0:, 2]]
    plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    #plt.plot(z_values,x_values, linestyle = "-")

    rms1 = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal1 = np.array(disttotal1+rms1)
    # print(rms)

plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Spot diagram: spherical surface first")
plt.show()
# print(disttotal)

rms_total1 = np.sqrt(disttotal1[-1]/301)
print(rms_total1)

# %%
# For the coma aberration plot, add 10 to the x values in the circle_points method in the class bundle.
# Using the curved surface first
# zx plot

r1 = oe.SphericalRefraction(
    z0=100, z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)
os1 = oe.OutputPlane(r.ray, z1=105, z2=250, z0=100, z01=105,
                     curvature=0.02, n1=1, n2=1.5168, a_radius=30)

disttotal1 = []
for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr1.intercept(i)
    sr1.plane_snells_intercept(i)
    sr1.plane_snells(i)
    os1.first_plane_intercept(i)
    os1.first_plane_point(i)
    os1.second_plane_intercept(i)
    os1.second_plane_point(i)
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])
    x_values = [A[0:, 0], B[0:, 0], C[0:, 0]]
    y_values = [A[0:, 2], B[0:, 2], C[0:, 2]]
    #plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    plt.plot(y_values, x_values, linestyle="-")

    rms1 = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal1 = np.array(disttotal1+rms1)
    # print(rms)

plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.title("Coma aberration plot: spherical surface first")
plt.show()
# print(disttotal)

rms_total1 = np.sqrt(disttotal1[-1]/301)
# print(rms_total1)

# %%

# For the coma aberration plot, add 10 to the x values in the circle_points method in the class bundle.
# Using the curved surface first
# focal plane plot

r1 = oe.SphericalRefraction(
    z0=100, z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)
os1 = oe.OutputPlane(r.ray, z1=105, z2=199.249226, z0=100,
                     z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)

disttotal1 = []
for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr1.intercept(i)
    sr1.plane_snells_intercept(i)
    sr1.plane_snells(i)
    os1.first_plane_intercept(i)
    os1.first_plane_point(i)
    os1.second_plane_intercept(i)
    os1.second_plane_point(i)
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])
    x_values = [A[0:, 0], B[0:, 0], C[0:, 0]]
    y_values = [A[0:, 2], B[0:, 2], C[0:, 2]]
    plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    #plt.plot(y_values,x_values, linestyle = "-")

    rms1 = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal1 = np.array(disttotal1+rms1)
    # print(rms)

plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Coma spot diagram: spherical surface first")
plt.show()
# print(disttotal)

rms_total1 = np.sqrt(disttotal1[-1]/301)
print(rms_total1)

# %%

# For the coma aberration plot, add 10 to the x values in the circle_points method in the class bundle.
# Using the plane surface first
# zx plot


sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=250, z0=5, z01=100,
                     curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

disttotal = []

for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr2.plane_snells_intercept(i)
    sr2.plane_snells(i)
    os2.first_plane_intercept(i)
    os2.first_plane_point(i)
    sr2.intercept(i)
    sr2.snells(i)
    sr2.propagate_ray(i)
    os2.second_plane_intercept(i)
    os2.second_plane_point(i)
    D = np.array([i.vertices()[-4]])
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [D[0:, 0], A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [D[0:, 2], A[0:, 2], B[0:, 2], C[0:, 2]]

    # print(y_values)
    #plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    plt.plot(z_values, x_values, linestyle="-")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)
    # print(rms)

plt.grid()
plt.xlabel("z (mm)")
plt.ylabel("x (mm)")
plt.title("Coma aberration plot: plane surface first")
plt.show()
# print(disttotal)

rms_total = np.sqrt(disttotal[-1]/301)
# print(rms_total)

# %%

# For the coma aberration plots, add 10 to the x values in the circle_points
# method in the class bundle from the ray.py file to produce them.
# Using the plane surface first
# focal plane plot (spot diagram)

sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=199.249226, z0=5,
                     z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

disttotal = []

for index, i in enumerate(bund2.propogate_circle(radius=[0, 2, 4, 6, 8, 10], num=[1, 20, 40, 60, 80, 100])):

    sr2.plane_snells_intercept(i)
    sr2.plane_snells(i)
    os2.first_plane_intercept(i)
    os2.first_plane_point(i)
    sr2.intercept(i)
    sr2.snells(i)
    sr2.propagate_ray(i)
    os2.second_plane_intercept(i)
    os2.second_plane_point(i)
    D = np.array([i.vertices()[-4]])
    A = np.array([i.vertices()[-3]])
    B = np.array([i.vertices()[-2]])
    C = np.array([i.vertices()[-1]])

    x_values = [D[0:, 0], A[0:, 0], B[0:, 0], C[0:, 0]]
    z_values = [D[0:, 2], A[0:, 2], B[0:, 2], C[0:, 2]]

    # print(y_values)
    plt.plot(i.vertices()[-1][0], i.vertices()[-1][1], ".")
    #plt.plot(z_values,x_values, linestyle = "-")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]
    disttotal = np.array(disttotal+rms)
    # print(rms)

plt.grid()
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Coma spot diagram: plane surface first")
plt.show()
# print(disttotal)

rms_total = np.sqrt(disttotal[-1]/301)
print(rms_total)
