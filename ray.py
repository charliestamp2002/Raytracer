#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:13:21 2022

@author: charliestamp
"""

import numpy as np
from sympy import Point3D, Plane
import matplotlib.pyplot as plt


class ray:

    def __init__(self, p=np.array([0.0, 0.0, 0.0]), k=np.array([0.0, 0.0, 0.0])):
        """


        Parameters
        ----------
        p : array
            Position of array. The default is np.array([0.0,0.0,0.0]).
        k : array, optional
            The direction vector of an array. The default is 
            np.array([0.0,0.0,0.0]).

        Raises
        ------
        Exception
            If parameter p or k have the wrong size (anything other 
            than 3-dimensional), an exception is raised.

        Returns
        -------
        None.

        """
        self._p = [p]
        self._k = [k]
        self.append(p, k)

        if len(self._p[-1]) != 3:
            raise Exception('ray parameter p has the incorrect size')
        if len(self._k[-1]) != 3:
            raise Exception('ray parameter k has the incorrect size')

    def __repr__(self):
        """


        Returns
        -------
        str
            An array composed of the position of the ray and the 
            direction of the ray.

        """

        return f'{self._p}, {self._k}'

    def p(self):
        """


        Returns
        -------
        array
            Returns the last position of the ray.

        """
        return self._p[-1]

    def k(self):
        """


        Returns
        -------
        array
            Returns the last direction of the ray.

        """
        return self._k[-1]

    def append(self, p, k):
        """


        Parameters
        ----------
        p : array
            The position of the ray.
        k : array
            The direction of the ray.

        Returns
        -------
        Appends a new position and normalised direction 
        to an existing list of arrays of rays.

        """
        list.append(self._p, p)

        k_length = np.sqrt((k[0]**2) + (k[1]**2) + (k[2]**2))
        k_norm = [k[0]/k_length, k[1]/k_length, k[2]/k_length]
        # I have calculated the normalised version of the direction here as the normalised version will be needed throughout.

        list.append(self._k, k_norm)

    def vertices(self):
        """


        Returns
        -------
        list
            Returns a list of all positions of the ray.

        """
        return self._p

    def directions(self):
        """


        Returns
        -------
        list
            Returns a list of all directions of the ray.

        """
        return self._k


class bundle(ray):

    def __init__(self, ray, radius=[], num=[]):
        """


        Parameters
        ----------
        ray : array
             a 2x3 matrix describing a ray's position and direction.
        radius : list
            Specifies the radius of each circle of ray starting positions
            to be created. The default is [0, 0, 0].
        num : list
            The number of starting ray positions generated at each circle 
            radius. The default is [0, 0, 0].

        Returns
        -------
        None.

        """

        self._radius = radius
        self._num = num

    def circle_points(self, radius, num):
        """


        Parameters
        ----------
        radius : list
            Specifies the radius of each circle of ray starting positions 
            to be created.
        num : list
             The number of starting ray positions generated at each circle 
             radius.

        Returns
        -------
        list
            Returns a list of starting ray positions. These positions only 
            have 2 dimensions(x and y). The z position will be appended in 
            the next method.

        """
        circles = []

        for radius, num in zip(radius, num):
            t = np.linspace(0, 2*np.pi, num, endpoint=False)
            x = radius * np.cos(t)
            y = radius * np.sin(t)

            circles.append(np.c_[x, y])

        return np.concatenate((circles[0], circles[1], circles[2], circles[3], circles[4], circles[5]))

    def circle_3dpoints(self, radius, num):
        """


        Parameters
        ----------
        radius : list
            Specifies the radius of each circle of ray starting positions 
            to be created.
        num : list
            The number of starting ray positions generated at each circle 
            radius.

        Returns
        -------
        array
            This returns an array of lists where each list is the starting 
            position of a ray. As stated,this appends a z position of 0 to 
            each ray created using the 'circle_points' method. 

        """

        xy = self.circle_points(radius, num)

        xy_list = xy.tolist()

        for list in xy_list:
            list.append(0)

        return np.array(xy_list)

    def propogate_circle(self, radius, num):
        """


        Parameters
        ----------
        radius : list
            Specifies the radius of each circle of ray starting positions
            to be created.
        num : list
            The number of starting ray positions generated at each circle
            radius.

        Returns
        -------
        array
            Returns an array with position and direction, where the positions
            are the circlepositions created using the prior methods and the 
            direction is [0,0,1] in all cases.

        """

        c = self.circle_3dpoints(radius, num)

        import ray as r

        self.rays = []
        for i in c:

            ray = r.ray(p=i.tolist(), k=[0, 0, 1])
            self.rays.append(ray)

        return np.array(self.rays)
