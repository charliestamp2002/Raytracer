#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:29:43 2022

@author: charliestamp
"""

import numpy as np

from sympy import Point3D, Plane
import matplotlib.pyplot as plt

import ray as r
import OpticalElement as oe

incorrect_size_ray_position = r.ray([1, 1, 1, 1], [2, 2, 2])
incorrect_size_ray_direction = r.ray([1, 1, 1], [2, 2, 2, 2])

# The kernel should raise the exception: 'ray parameter p [ or k] has the incorrect size,
# which it does.
# %%
v = r.ray([1, 1, 1], [2, 2, 2])

print(v.__repr__())

# Thus the 'repr' function successfully performs its function.

# %%
ray_1 = [1, 5, 9]
ray_2 = [6, 0, 4]
ray_3 = [2, 2, 10]
ray_4 = [3, 3, 3]


v.append(ray_1, ray_2)

v.append(ray_3, ray_4)

print("The last point in the list of points is", v.p())
print("The last direction in the list of direction is", v.k())


# As expected, if we append ray_3 and ray_4, the last point and direction are ray_3
# and ray_4 normalised, respectively.


# %%

print("The list of points are", v.vertices())
print("The list of directions are", v.directions())

# The first point and first direction prints out twice because the first direction is presented as both unnormalised and then normalised, both at the same point.

# %%

# Testing whether a ray with only non-zero starting z position and direction propagates
# correctly while only refracting through a spherical surface with z0 = 100.

c = r.ray([0, 0, -5], [0, 0, 1])

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=250, z2=300, z0=100, z01=250,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

print("The intercept of the ray c with the spherical surface is", l.intercept(c))

# This is to be expected, if the ray has only a z direction, the ray must intercept with
# the spherical surface at z0.

print("The refracted direction is", l.snells(c))

l.propagate_ray(c)

os.first_plane_intercept(c)

print("The intercept of the ray with the output plane is",
      os.first_plane_intercept(c))


os.first_plane_point(c)

plt.plot(np.array(c.vertices())[:, 2], np.array(
    c.vertices())[:, 0], label='Test plot 1')
plt.legend()
plt.grid()
plt.show()

# The plot shows both l.propagate_ray(c) and os.first_plane_point(c) succesfully appends
# the correct ray to the vertices method.

# %%

# Testing whether a ray with non-zero x and y positions but with zero x and y directions
# propagate correctly.

d = r.ray([0.1, 0.3, -5], [0, 0, 1])

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=250, z2=300, z0=100, z01=250,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

l.intercept(d)

print("The intercept of the ray d with the spherical surface is", l.intercept(d))

# This is expected as the ray will meet the spherical surface slightly past z0 as the
# ray starts above the z axis.
# The x and y part of the intercepts will be the same as the ray has no x and y direction.

l.snells(d)

print("The refracted direction is", l.snells(d))

# This is expected as the x direction should be negative, and the z direction should
# still be positive.

l.propagate_ray(d)

os.first_plane_intercept(d)

print("The intercept of the ray with the output plane is",
      os.first_plane_intercept(d))

# This succesfully intercepts with the output plane at z = 250 mm.


os.first_plane_point(d)

plt.plot(np.array(d.vertices())[:, 2], np.array(
    d.vertices())[:, 0], label='Test plot 2')
plt.legend()
plt.grid()
plt.show()

# The plot shows both l.propagate_ray(d) and os.first_plane_point(d) succesfully
# appends the correct ray to the vertices method.

# %%

# Testing whether a ray with non-zero x and y positions but with zero x and y directions propagate correctly.

e = r.ray([0.1, 0.3, -5], [0.1, 0.05, 1])

l = oe.SphericalRefraction(
    z0=100, z01=250, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=250, z2=300, z0=100, z01=250,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

l.intercept(e)

print("The intercept of the ray e with the spherical surface is", l.intercept(e))

# This is expected as the ray will meet the spherical surface slightly past z0 as
# the ray starts above the z axis.
# The x and y components of the starting directions of the ray are also non-zero,
# thus the x and y components of the intercept  will be non-zero.

l.snells(e)

print("The refracted direction is", l.snells(e))

# This is expected as the x and y direction should be negative as the ray should
# refract back towards the optical axis, and the z direction should still be positive,.

l.propagate_ray(e)

os.first_plane_intercept(e)

print("The intercept of the ray with the output plane is",
      os.first_plane_intercept(e))

# This succesfully intercepts with the output plane at z = 250 mm.


os.first_plane_point(e)

plt.plot(np.array(e.vertices())[:, 2], np.array(
    e.vertices())[:, 0], label='Test plot 3')
plt.legend()
plt.grid()
plt.show()

# The plot shows both l.propagate_ray(e) and os.first_plane_point(e) succesfully
# appends the correct ray to the vertices method.

# Therefore, these methods succesfully propagate a ray when all of the components of the starting position and direction are non-zero.

# %%

# Testing whether my bundle method works for creating a circle of points:

bund = r.bundle(r.ray, radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[
                1, 10, 20, 30, 40, 50])
bund.circle_points(radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[
                   1, 10, 20, 30, 40, 50])

print(bund.circle_points(
    radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[1, 10, 20, 30, 40, 50]))

# The bundle creates an initial starting position of x and y positions, arranged
# in a circle.

# plot to prove this:


plt.scatter(np.array(bund.circle_points(radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[1, 10, 20, 30, 40, 50]))[:, 0], np.array(
    bund.circle_points(radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[1, 10, 20, 30, 40, 50]))[:, 1], label='Test plot 4')
plt.legend()
plt.grid()
plt.show()

bund.circle_3dpoints(radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[
                     1, 10, 20, 30, 40, 50])

print(bund.circle_3dpoints(
    radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[1, 10, 20, 30, 40, 50]))

# As expected, the z position of 0 has been appended to the bundle


# To return an array of points to use in the rms plot, the following method
# appends the direction [0,0,1] to a ray.

bund.propogate_circle(radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[
                      1, 10, 20, 30, 40, 50])

l = oe.SphericalRefraction(
    z0=100, z01=200, curvature=0.03, n1=1, n2=1.5, a_radius=30)
os = oe.OutputPlane(r.ray, z1=200, z2=300, z0=100, z01=200,
                    curvature=0.03, n1=1, n2=1.5, a_radius=30)

disttotal = []

for i in bund.propogate_circle(radius=[0, 0.1, 0.2, 0.3, 0.4, 0.5], num=[1, 10, 20, 30, 40, 50]):
    a = l.intercept(i)
    b = l.snells(i)
    c = l.propagate_ray(i)
    d = os.first_plane_intercept(i)
    e = os.first_plane_point(i)

    print(i.vertices())

    plt.plot(i.vertices()[-1][0], i.vertices()
             [-1][1], ".", label="test plot 5")

    rms = [(i.vertices()[-1][0])**2 + (i.vertices()[-1][1])**2]

    disttotal = np.array(disttotal+rms)

plt.show()


rms_total = np.sqrt(disttotal[-1]/151)
print(rms_total)

# the rms value shown is for the parameters given in task 9. As expected,
# the plot shows that the rms of these rays will be small. The rms value calculated
# re-affirms this
# %%

r1 = r.ray([10, 0, 0], [0, 0, 1])
sr1 = oe.SphericalRefraction(
    z0=100, z01=105, curvature=0.02, n1=1, n2=1.5168, a_radius=30)
os1 = oe.OutputPlane(r.ray, z1=105, z2=300, z0=100, z01=105,
                     curvature=0.02, n1=1, n2=1.5168, a_radius=30)


sr1.intercept(r1)
print("The intercept of the ray c with the spherical surface is", sr1.intercept(r1))
sr1.snells(r1)
print("The refracted direction after the ray meets the spherical surface is", sr1.snells(r1))
sr1.propagate_ray(r1)
sr1.plane_snells_intercept(r1)
print("The intercept with the ray as it meets the plane surface after the spherical surface is",
      sr1.plane_snells_intercept(r1))
sr1.plane_snells(r1)
print("The refracted direction after the ray meets the plane surface is",
      sr1.plane_snells(r1))
os1.first_plane_intercept(r1)
print("The intercept with the ray as it meets the plane surface after the spherical surface is",
      os1.first_plane_intercept(r1))
os1.first_plane_point(r1)
os1.second_plane_intercept(r1)
print("The intercept with the ray as it meets the output plane after the plane surface of the plano-convex lens is",
      os1.second_plane_intercept(r1))
os1.second_plane_point(r1)


plt.plot(np.array(r1.vertices())[:, 2], np.array(
    r1.vertices())[:, 0], label='Test plot 6')
plt.legend()
plt.grid()
plt.show()

# %%

# Testing whether the plano-convex lens works when the plane surface is first, and
# the spherical surface is second for the parameters given in task 15:


r2 = r.ray([10, 0, 0], [0, 0, 1])

sr2 = oe.SphericalRefraction(
    z0=5, z01=100, curvature=-0.02, n1=1, n2=1.5168, a_radius=30)
os2 = oe.OutputPlane(r.ray, z1=100, z2=300, z0=5, z01=100,
                     curvature=-0.02, n1=1, n2=1.5168, a_radius=30)

sr2.plane_snells_intercept(r2)
print("The intercept of the ray c with the plane surface is",
      sr2.plane_snells_intercept(r2))
sr2.plane_snells(r2)
print("The refracted direction after the ray meets the plane surface is",
      sr2.plane_snells(r2))
os2.first_plane_intercept(r2)
os2.first_plane_point(r2)
sr2.intercept(r2)
print("The intercept of the ray c with the spherical surface after refracting past the plane surface is", sr2.intercept(r2))
sr2.snells(r2)
print("The refracted direction after the ray meets the spherical surface is", sr2.snells(r2))
sr2.propagate_ray(r2)
os2.second_plane_intercept(r2)
print("The intercept with the ray as it meets the output plane after the spherical surface of the plano-convex lens is",
      os2.second_plane_intercept(r2))
os2.second_plane_point(r2)


plt.plot(np.array(r2.vertices())[:, 2], np.array(
    r2.vertices())[:, 0], label='test plot 7')
plt.grid()
plt.legend()
plt.show()

# As the focal length for both orientations of the plano-convex lens is 100,
# both rays should meet at 200mm.
# As you can see, both rays meet the optical axis at 200mm. Therefore,
# the plano-convex lens works at both orientations as expected.
