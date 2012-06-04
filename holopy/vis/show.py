# Copyright 2011, Vinothan N. Manoharan, Thomas G. Dimiduk, Rebecca
# W. Perry, Jerome Fung, and Ryan McGorty
#
# This file is part of Holopy.
#
# Holopy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Holopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Holopy.  If not, see <http://www.gnu.org/licenses/>.

"""
A general show method that can display most holopy and scatterpy objects in a
sensible way.  

.. moduleauthor:: Thomas G. Dimiduk <tdimiduk@physics.harvard.edu>
"""

import holopy as hp
import numpy as np
import scatterpy

class VisualizationNotImplemented(Exception):
    def __init__(self, o):
        self.o = o
    def __str__(self):
        return "Visualization of object of type: {0} not implemented".format(
            self.o.__class__.__name__)
    

def show(o,color=(0,0,1)):
    """
    Visualize a scatterer, hologram, or reconstruction

    Parameters
    ----------
    o: :class:`scatterpy.scatterer.Scatterer`, :class:`holopy.hologram.Hologram`, or :class:`holopy.analyze.reconstruct.Reconstruction`
       Object to visualize

    Notes
    -----
    Loads plotting library the first time it is required (so that we don't have
    to import all of mayavi just to load holopy)
    """
    
    if isinstance(o, scatterpy.scatterer.SphereCluster):
        import vis3d
        vis3d.show_sphere_cluster(o,color)
        return
    
    elif isinstance(o, (list, tuple)):
        o = np.dstack(o)
    if isinstance(o, (hp.Hologram, hp.analyze.reconstruct.Reconstruction,
                        np.ndarray)):
        import vis2d
        vis2d.show(o)
    else:
        raise VisualizationNotImplemented(o)