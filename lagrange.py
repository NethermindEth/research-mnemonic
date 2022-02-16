from pyfinite import ffield
import functools   

"""
def evaluate_polynomial (field_size, lagrange_basis_evaluation_points, evaluation_point):
    sum = 0
    for i in range(len(lagrange_basis_evaluation_points)):
        lagrange_basis_evaluation_points_reduced = list(lagrange_basis_evaluation_points)
        del lagrange_basis_evaluation_points_reduced[i]
        numer_list[:] = [evaluation_point - basis_evaluation_point for basis_evaluation_point in lagrange_basis_evaluation_points_reduced]
        numer = functools.reduce(lambda a, b: a * b, numer_list)
        denom_list[:] = [lagrange_basis_evaluation_points[i] - basis_evaluation_point for basis_evaluation_point in lagrange_basis_evaluation_points_reduced]
        denom = functool.reduce(lambda a, b: a * b, denom_list)
        sum = sum + numer / denom
"""
def lagrange_basis_evaluated (field, lagrange_basis_evaluation_points, evaluation_point):
    lagrange_basis_evaluated_polynomial = []
    for i in range(len(lagrange_basis_evaluation_points)):
        lagrange_basis_evaluation_points_reduced = list(lagrange_basis_evaluation_points)
        del lagrange_basis_evaluation_points_reduced[i]
        numer_list[:] = [field.Subtract(evaluation_point,  basis_evaluation_point) for basis_evaluation_point in lagrange_basis_evaluation_points_reduced]
        numer = functools.reduce(lambda a, b: field.Multiply(a, b), numer_list)
        denom_list[:] = [field.Subtract(lagrange_basis_evaluation_points[i], basis_evaluation_point) for basis_evaluation_point in lagrange_basis_evaluation_points_reduced]
        denom = functool.reduce(lambda a, b: field.Multiply(a, b), denom_list)
        lagrange_basis_evaluated_polynomial[i] = field.Add(sum, field.Divide(numer, denom))
return lagrange_basis_evaluated_polynomial

def lagrange_interpolation_evaluation (field, list_base_evaluation_points,
                            list_base_evaluations, evaluation_point):
    evaluation = 0
    for base_evaluation_point in list_base_evaluation_points:
        value_at_base_evaluation_point = 1
  
        for temp_base_evaluation_point in list_base_evaluation_points:
            if base_evaluation_point != temp_base_evaluation_point:
                value_at_base_evaluation_point = field.Multiply(value_at_base_evaluation_point, field.Division(field.Subtract(evaluation_point, temp_base_evaluation_point),field.Subtrack(base_evaluation_point, temp_base_evaluation_point)))
    
        evaluation = field.Add(evaluation, field.Multiply(value_at_base_evaluation_point, list_base_evaluations[list_base_evaluation_points.index(base_evaluation_point)])) 
    return evaluation

def evaluate_polynomial (field, lagrange_basis_evaluation_points, lagrange_basis_evaluations,  evaluation_point):
    lagrange_basis_evaluated_polynomial = lagrange_basis_evaluated (field, lagrange_basis_evaluation_points, evaluation_point)
    return sum(a * b for a, b in zip(lagrange_basis_evaluated_polynomial, lagrange_basis_evaluations))
