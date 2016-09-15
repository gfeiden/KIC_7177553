# Basic Mass Tracks

Basic mass tracks contain the most sought after data from stellar models (namely stellar fundamental properties) as a function of age. 

### Naming convention

A typical file name looks like `mXXXX_COMP_sZZZ_sA_yYY_mltC.CCC(_magBBkG).trk`. A quick breakdown of the various components:

 - mXXXX. m represents the mass of the star, while the number XXXX is the mass of the star in solar units multiplied by 1000. (e.g., 1.45 Msun --> m1450)

 - COMP. Solar abundance distribution. (e.g., GS98 for Grevesse & Suaval 1998)

 - sZZZ. Initial metallicity, where s is a letter indicative of the sign (p = +, m = -) and the quantity ZZZ is the metallicity with respect to solar multiplied by 100. (e.g, -0.10 dex --> m010)
 
 - sA. Alpha abundance variation, where s is a letter indicative of the sign (p = +, m = -) and the quantity A is the value of [alpha/Fe] multiplied by 10. (e.g., [alpha/Fe] = +0.2 --> p2)

 - yYY. Initial helium mass fraction, where YY is the initial helium mass fraction multiplied by 100. (e.g., Y = 0.28 --> y28)

 - mltC.CCC. Mixing length theory alpha (number of pressure scale heights contained in one "mixing length"). C.CCC is the numerical value of alpha used in the code.

 - magBBkG. Surface magnetic field strength where BB is the value of the average surface magnetic field strength in kG multiplied by 10. (e.g., 3.0 kG --> mag30kG)


