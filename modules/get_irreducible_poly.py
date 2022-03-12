import json
import galois
from pyrsistent import m


def get_irreducible_poly(degree:int):
	with open("modules/polynomials.json", "r") as file:
		polynomials = json.load(file)

	if degree not in polynomials:
		polynomials[degree] = galois.irreducible_poly(2**degree, degree).string
		with open("modules/polynomials.json", "w") as file:
			json.dump(polynomials, file, indent=4)

	return polynomials[degree]

#Initialize polynomials, if wanted:
#for degree in range(3,31):
#	get_irreducible_poly(11*degree)


lst = galois.irreducible_poly(order=2**(24*11),degree=24*11,method='random')