#!/usr/bin/python
#
import dmestar as dsep
from numpy import arange

masses  = [1.043, 0.986]
Bfields = arange(0.5, 2.1, 0.5)*1.0e3
for m in masses:
    for B in Bfields:
        star = dsep.Model(m, -0.1, tau_atm = 10, atm = "phx", eos = "feos",
	                  mixture="GS98", final_age = 1.0e10, b_field="on",
                          b_surf = B, b_pert_age = 3.0e-4, fc_tach=0.5,
                          b_rad_prof="gauss", dynamo="rot")
        star.construct()
        star.evolve()
        star.cleanup()
