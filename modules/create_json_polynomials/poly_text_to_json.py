"""Data wrangling: Turn the powers from the polynomial paper into a JSON of polynomial strings.

The raw power data has been obtained from:

Rajski, J., & Tyszer, J. (2003). Primitive polynomials over GF(2) of degree up to 660 with 
uniformly distributed coefficients. Journal of Electronic Testing, 19(6), 645-657.
"""

import json
import galois
from numpy import zeros


polynomials = {}

with open("modules/create_json_polynomials/polynomials_raw.txt") as file:
	for line in file:
		#Each line has either 1 or 3 polynomials, so we split as follows:
		line_as_list = line.rstrip('\n').split(' ')
		line_as_list = list(map(int, line_as_list))
		if len(line_as_list) == 15:
			polynomials[line_as_list[0]] = line_as_list[0:5]
			polynomials[line_as_list[5]] = line_as_list[5:10]
			polynomials[line_as_list[10]] = line_as_list[10:15]
		else:
			polynomials[line_as_list[0]] = line_as_list[0:5]

#Now turn the lists of integers to a string polynomial.
for degree in polynomials:
	list_of_coefficients = zeros(degree+1, dtype=int)

	for power in polynomials[degree]:
		list_of_coefficients[power] = 1

	current_poly = galois.Poly(list_of_coefficients)
	polynomials[degree] = current_poly.string

#Save to JSON:
with open("modules/create_json_polynomials/polynomials.json", "w") as file:
	json.dump(polynomials, file, indent=4)