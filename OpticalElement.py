#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:19:34 2022

@author: charliestamp
"""
import numpy as np
from sympy import Point3D, Plane
import matplotlib.pyplot as plt


class OpticalElement:

    def propagate_ray(self, ray):
        """


        Parameters
        ----------
        ray : array
            a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        This method returns nothing but works to append the intercept 
        position of the intercept with the spherical surface to the 
        list of positions the ray already has at that stage. This is 
        so that, when calling the vertices method in the ray class, it 
        successfully works.

        """

        intercept = self.intercept(ray)
        refracted_dir = self.snells(ray)
        ray.append(intercept, ray.k())


class SphericalRefraction(OpticalElement):

    def __init__(self, z0, z01,  curvature, n1, n2, a_radius):
        """


        Parameters
        ----------
        z0 : float
            The intercept of the spherical surface with the z-axis.
        z01 : float
            The z position of the first plane.
        curvature : float
            The curvature of the surface. The radius of the spherical
            surface is the magnitude of the reciprocal of the surface
        n1 : float
            The refractive index of the air to the left side of 
            the spherical surface in the case where the ray is just 
            refracting through the spherical surface (task 10). 
            The refractive index outside the glass in the case 
            where we are investigating a plano convex lens (task 15).
        n2 : float
            The refractive index of the surface in the case where 
            the ray is just refracting through the spherical surface 
            (task 10). The refractive index of the glass in the case 
            where we are investigating a plano convex lens (task 15).
        a_radius : float
            The aperture radius: the maximum vertical distance of the 
            surface from the optical axis.            

        Returns
        -------
        None.

        """

        self._z0 = z0
        self._curvature = curvature
        self._n1 = n1
        self._n2 = n2
        self._a_radius = a_radius
        self._z01 = z01

    def intercept(self, ray):
        """


        Parameters
        ----------
        ray : list
            a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        array
            The returned value is the array of the intercept of the 
            ray and the spherical surface. There are two if statements below. 
            The purpose of each is to determine whether the Spherical surface
            is first when propogating the ray through the plano-convex lens. 
            As a guide, if z0 (the z position of the first plane) is less than 
            z01 (the z position of the plane part of the plano-convex lens), 
            andthe curvature is greater than zero, the spherical surface part 
            must be the first surface the ray meets. Thus, we implement the 
            intercept method for a spherical surface as opposed to a plane. On 
            the contrary, if the curvature is less than zero, this signifies the 
            intercept of the spherical surface is the second intercept at the far 
            side of the sphere, i.e. when the plane of the plano-convex lens is 
            the first object that the ray meets. This is the purpose of the second
            'if' statement, to ensure the ray intercepts as it would with a plane 
            as opposed to a spherical surface. These two if statements will be 
            deployed in most methods after this method.To ensure the ray either 
            intercepts/ refracts as it would when it meets either the spherical 
            surface or the plane and in the correct order.

        """

        if self._z0 < self._z01 and self._curvature > 0:
            # if spherical surface is first:

            P = ray.p()
            k = ray.k()
            # Optical centre of the sphere
            O = np.array([0.0, 0.0, self._z0 + 1/np.absolute(self._curvature)])

            # the vector of r: a point minus the optical centre of the sphere.
            rv = P - O

            square_rk = (np.dot(rv, k))**2
            mod_rv = np.sqrt(rv[0]**2 + rv[1]**2 + rv[2]**2)

            r_R = mod_rv**2 - (1/np.absolute(self._curvature))**2

            l1 = np.array(-np.dot(rv, k) + np.sqrt(square_rk - r_R))
            l2 = np.array(-np.dot(rv, k) - np.sqrt(square_rk - r_R))
            # Due to the quadratic nature of l, there will be two solutions to l, l1 and l2.

            if (square_rk - r_R) < 0:
                return None

            Q1 = np.add(ray.p(), l2*k)
            Q2 = np.add(ray.p(), l1*k)

            if self._curvature < 0 and Q1[2] < Q2[2]:
                return Q2

            if self._curvature < 0 and Q2[2] < Q1[2]:
                return Q1

            if self._curvature > 0 and Q2[2] < Q1[2]:
                return Q2

            if self._curvature > 0 and Q2[2] > Q1[2]:
                return Q1

            # the purpose of these ifs are to ensure the ray intercepts at either
            # the closer side or the longer side according to curvature and the
            # length of Q1 or Q2.

        if self._z0 < self._z01 and self._curvature < 0:
            # if plane surface first:

            P = self.plane_snells_intercept(ray)
            k = self.plane_snells(ray)

            O = np.array([0.0, 0.0, self._z0 + 1/np.absolute(self._curvature)])
            # Optical centre of the sphere

            rv = P - O
            # the vector of r: a point minus the optical centre of the sphere.

            square_rk = (np.dot(rv, k))**2
            mod_rv = np.sqrt(rv[0]**2 + rv[1]**2 + rv[2]**2)

            r_R = mod_rv**2 - (1/np.absolute(self._curvature))**2

            l1 = np.array(-np.dot(rv, k) + np.sqrt(square_rk - r_R))
            l2 = np.array(-np.dot(rv, k) - np.sqrt(square_rk - r_R))

            if (square_rk - r_R) < 0:
                return None

            Q1 = np.add(P, l2*k)
            Q2 = np.add(P, l1*k)

            if self._curvature < 0 and Q1[2] < Q2[2]:
                return Q2

            if self._curvature < 0 and Q2[2] < Q1[2]:
                return Q1

            if self._curvature > 0 and Q2[2] < Q1[2]:
                return Q2

            if self._curvature > 0 and Q2[2] > Q1[2]:
                return Q1

    def snells(self, ray):
        """


        Parameters
        ----------
        ray : array
            a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        refracted_direction : array
            The refracted direction of the ray as it passes from the
            medium n1 into the medium n2 through the spherical surface.

        """

        if self._z0 < self._z01 and self._curvature > 0:
            # if spherical surface is first:

            O = np.array([0.0, 0.0, self._z0 + 1/np.absolute(self._curvature)])

            normal = O - self.intercept(ray)

            ray_vec = np.array(ray.k())
            # this is the incident ray vector
            ri = self._n1/self._n2

            nhat = normal/np.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)

            c = np.dot(nhat, ray_vec)

            a = ri*ray_vec

            b = ri*c

            d = ri**2

            e = 1-(c**2)

            f = np.sqrt(1 - d*e)

            refracted_direction = a + (b - f)*-nhat

        if self._z0 < self._z01 and self._curvature < 0:
            # if plane surface first:

            O = np.array([0.0, 0.0, self._z0 + 1/np.absolute(self._curvature)])

            normal = self.intercept(ray) - O

            ray_vec = np.array(self.plane_snells(ray))
            # this is the incident ray vector
            ri = self._n2/self._n1
            # n1 and n2 have been flipped here as the ray will be inside the
            # glass at this point.

            nhat = normal/np.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)

            c = np.dot(nhat, ray_vec)

            a = ri*ray_vec

            b = ri*c

            d = ri**2

            e = 1-(c**2)

            f = np.sqrt(1 - d*e)

            refracted_direction = a + (b - f)*-nhat

            # refracted_direction has been split up into smaller chunks in
            # both if statements to make the final expression easier to write.

        return refracted_direction

    def plane_snells_intercept(self, ray):
        """


        Parameters
        ----------
        ray : array
             a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        intercept_point : array
            The intercept of the ray when it meets a plane parallel 
            to the x-y plane. The intercept of the ray between a plane 
            has been calculated by calculating the intercept between a 
            line (ray) and a plane. This has been simplified as all the 
            planes specified in this project are parallel to the xy plane.
            Thus, we do not need to necessarily specify a plane surface 
            to calculate the intercept between a line and a plane, only 
            the z point of the plane. This is what self._z01 acts as, the 
            z point in the plane.

        """

        if self._z0 < self._z01 and self._curvature > 0:
            # if spherical surface is first:

            P = self.intercept(ray)
            k = self.snells(ray)

            scale_factor = (self._z01-P[2])/k[2]

            intercept_point = np.array(
                [P[0], P[1], P[2]]) + (scale_factor * np.array([k[0], k[1], k[2]]))

        if self._z0 < self._z01 and self._curvature < 0:
            # if plane surface first:

            P = ray.p()
            k = ray.k()

            scale_factor = (self._z01-P[2])/k[2]

            intercept_point = np.array(
                [P[0], P[1], P[2]]) + (scale_factor * np.array([k[0], k[1], k[2]]))

        return intercept_point

    def plane_snells(self, ray):
        """


        Parameters
        ----------
        ray : array
             a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        plane_direction : array
            The direction of the ray after it refracts through a plane 
            parallel to the xy plane.

        """

        if self._z0 < self._z01 and self._curvature > 0:
            # if spherical surface is first:

            nhat = np.array([0, 0, 1])

            ray_vec = np.array(self.snells(ray))

            ri = self._n2/self._n1

            c = np.dot(nhat, ray_vec)

            a = ri*ray_vec

            b = ri*c

            d = ri**2

            e = 1-(c**2)

            f = np.sqrt(1 - d*e)

            plane_direction = a + (b - f)*-nhat

        if self._z0 < self._z01 and self._curvature < 0:
            # if plane surface first:

            nhat = np.array([0, 0, 1])

            ray_vec = np.array(ray.k())

            ri = self._n1/self._n2

            c = np.dot(nhat, ray_vec)

            a = ri*ray_vec

            b = ri*c

            d = ri**2

            e = 1-(c**2)

            f = np.sqrt(1 - d*e)

            plane_direction = a + (b - f)*-nhat

        return plane_direction


# %%%


class OutputPlane(SphericalRefraction):

    def __init__(self, ray, z1, z2, z0, z01, curvature, n1, n2, a_radius):
        """


        Parameters
        ----------
        ray : array
            a 2x3 matrix describing a ray's position and direction.
        z : float
            As all planes defined in this exercise are parralel to 
            the x-y plane, this parameter describes the z position 
            of the plane.
        z0 : float
            The intercept of the surface with the z-axis.
        curvature : float
           The curvature of the surface. The radius of the spherical
            surface is the magnitude of the reciprocal of the surface.
        n1 : float
             The refractive index of the surface to the left side
            of the spherical surface.
        n2 : float
            The refractive index of the surface to the right side
            of the spherical surface.
        a_radius : float
             The aperture radius: the maximum vertical distance of the
             surface from the optical axis.

        Returns
        -------
        None.


        """

        self._z0 = z0
        self._z01 = z01
        self._curvature = curvature
        self._n1 = n1
        self._n2 = n2
        self._a_radius = a_radius
        self._z1 = z1
        self._z2 = z2

    def plane(self, ray):
        """


        Parameters
        ----------
        ray : array
        a 2x3 matrix describing a ray's position and direction.


        Returns
        -------
        p1.equation() : string
            This returns the equation of the plane described by 
            3 points in the plane in Cartesian form. 

        """

        p1 = Plane(Point3D(1, 4, self._z1), Point3D(
            2, 5, self._z1), Point3D(3, 7, self._z1))

        return p1.equation()

    def first_plane_intercept(self, ray):
        """


        Parameters
        ----------
        ray : array
            a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        point : array
            The point at which the ray, travelling from the spherical 
            surface intercept, intercepts the plane.

        """

        if self._z0 < self._z01 and self._curvature > 0:
            # if spherical surface is first:

            intercept = self.intercept(ray)
            rfrc_direction = self.snells(ray)

            a = (self._z1 - intercept[2])/(rfrc_direction[2])

            point = np.array([intercept[0], intercept[1], intercept[2]]) + (
                a * np.array([rfrc_direction[0], rfrc_direction[1], rfrc_direction[2]]))

        if self._z0 < self._z01 and self._curvature < 0:
            # if plane surface first:

            P = ray.p()
            k = ray.k()

            intercept = self.plane_snells_intercept(ray)
            rfrc_direction = self.plane_snells(ray)

            a = (self._z1 - intercept[2])/(k[2])

            point = np.array([intercept[0], intercept[1], intercept[2]]
                             ) + (a * np.array([k[0], k[1], k[2]]))

        return point

    def second_plane_intercept(self, ray):
        """


        Parameters
        ----------
        ray :  array
             a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        point : array
            Returns the position of the output plane.

        """

        if self._z0 < self._z01 and self._curvature > 0:
            # if spherical surface is first:

            intercept = self.plane_snells_intercept(ray)

            rfrc_direction = self.plane_snells(ray)

            a = (self._z2 - intercept[2])/(rfrc_direction[2])

            point = np.array([intercept[0], intercept[1], intercept[2]]) + (
                a * np.array([rfrc_direction[0], rfrc_direction[1], rfrc_direction[2]]))

        if self._z0 < self._z01 and self._curvature < 0:
            # if plane surface first:

            intercept = self.intercept(ray)

            rfrc_direction = self.snells(ray)

            a = (self._z2 - intercept[2])/(rfrc_direction[2])

            point = np.array([intercept[0], intercept[1], intercept[2]]) + (
                a * np.array([rfrc_direction[0], rfrc_direction[1], rfrc_direction[2]]))

        return point

    def first_plane_point(self, ray):
        """


        Parameters
        ----------
        ray : array
            a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        None.

        """

        ray.append(self.first_plane_intercept(ray), ray.k())

    def second_plane_point(self, ray):
        """


        Parameters
        ----------
        ray : array
            a 2x3 matrix describing a ray's position and direction.

        Returns
        -------
        None.

        """

        ray.append(self.second_plane_intercept(ray), ray.k())
