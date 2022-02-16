from pyfinite import ffield
import functools   

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
