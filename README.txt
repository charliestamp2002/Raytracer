This raytracer project is a project I did in Winter 2022 as part of my 2nd Year Computing Lab. Grade = 76%

In order to run the 4 .py files (ray.py, OpticalElement.py, tests.py, and plots.py) as intended, run the ray.py file first. This has the ray class and the bundle class. The reason for the bundle class being in this file is because bundle inherits from the ray class. 

After you have ran the ray.py file, run the OpticalElement.py file. 

You can then run the whole plots.py file in one. In order to get the coma aberration plots, once you have ran the file and created all the plots for the other plots referenced in the report, go back to the ray.py file and go to the 'circle_points' method in the bundle class. Go to the line:  'x = radius * np.cos(t)' (line 187) and add 10. The following line should read now:  'x = radius * np.cos(t) + 10'. Get rid off the 10 to create all the other plots shown in the report.

To do the testing in the test.py file. Do it section by section (i.e. do not run it all at once). This is because part of the testing is that certain errors and exceptions are raised if certain values are inputted.

All the imported modules from other .py files have been included in each module. So, you will not need to add anything extra to produce the plots or do the testing. If for some reason, they are not included, at the top of the ray.py file and the OpticalElement.py file import these three modules:

import numpy as np
from sympy import Point3D, Plane
import matplotlib.pyplot as plt

For the plots and tests.py file, import these modules:

import numpy as np

from sympy import Point3D, Plane
import matplotlib.pyplot as plt

import ray as r
import OpticalElement as oe
