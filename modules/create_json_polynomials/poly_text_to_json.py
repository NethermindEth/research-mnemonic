import json
import galois
from numpy import zeros


def poly_text_to_json():
	"""Turn the powers from the polynomial paper into a JSON of polynomial strings. 
	
	Quick-and-dirty code, but gets the work done."""

	polynomials = {}

	with open("modules/create_json_polynomials/polynomials_raw.txt") as file:
		for line in file:
			#Each line has 3 polynomials, so we split as follows:
			line_as_list = line.rstrip('\n').split(' ')
			line_as_list = list(map(int, line_as_list))
			if len(line_as_list) == 15:
				polynomials[line_as_list[0]] = line_as_list[0:5]
				polynomials[line_as_list[5]] = line_as_list[5:10]
				polynomials[line_as_list[10]] = line_as_list[10:15]
			else:
				polynomials[line_as_list[0]] = line_as_list[0:5]

	#Now turn the lists of integers to a string polynomial. Let us also certify primtiveness:
	non_primitive_polys = []
	for degree in polynomials:
		list_of_coefficients = zeros(degree+1, dtype=int)

		for power in polynomials[degree]:
			list_of_coefficients[power] = 1

		current_poly = galois.Poly(list_of_coefficients)
		primitive = galois.is_primitive(current_poly)
		if not primitive:
			non_primitive_polys.append(degree)
		polynomials[degree] = current_poly.string
		print("Processed degree " + str(degree) + ", non-primitives: ")
		print(non_primitive_polys)

	#Save to JSON:
	with open("modules/create_json_polynomials/polynomials.json", "w") as file:
		json.dump(polynomials, file, indent=4)
	
poly_text_to_json()