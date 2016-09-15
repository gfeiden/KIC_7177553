#!/usr/bin/python
#
import dmestar as dsep
from numpy import arange

masses  = [1.043, 0.986]
for m in masses:
    star = dsep.Model(0.986, 0.0, tau_atm = 10, atm = "phx", eos = "feos",
                      mixture="GS98", final_age = 1.0e10, b_field="off",
                      b_surf = 0.0, b_pert_age = 3.0e-4, fc_tach=0.5,
                      b_rad_prof="gauss", dynamo="rot")
    star.construct()
    star.evolve()
    star.cleanup()
