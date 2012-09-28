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
'''
Test fortran-based multilayered Mie calculations and python interface.  

.. moduleauthor:: Vinothan N. Manoharan <vnm@seas.harvard.edu>
.. moduleauthor:: Thomas G. Dimiduk <tdimiduk@physics.harvard.edu>
'''
from __future__ import division

from ...core import Optics, ImageSchema
from .common import verify
from ..theory import Mie
from ..scatterer import CoatedSphere

from nose.plugins.attrib import attr

@attr('medium')
def test_Shell():
    s = CoatedSphere(center=[7.141442573813124, 7.160766866147957, 11.095409800342143],
              n=[(1.27121212428+0j), (1.49+0j)], r=[0.960957713253-0.0055,
                                                    0.960957713253]) 

    optics = Optics(wavelen=0.658, index=1.36, polarization=[1.0, 0.0],
              pixel_scale=[0.071333, 0.071333])
    
    t = ImageSchema(200, optics = optics)

    h = Mie.calc_holo(s, t, scaling = 0.4826042444701572)

    verify(h, 'shell')