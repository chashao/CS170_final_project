#!/usr/bin/env python

from __future__ import division
import argparse
from pulp import *
from collections import defaultdict

"""
===============================================================================
  Please complete the following function.
===============================================================================
"""

def solve(P, M, N, C, items, constraints):
    """
    Write your amazing algorithm here.

    Return: a list of strings, corresponding to item names.
    """
    Items = []
    weight_dict = dict()
    cost_dict = dict()
    earn_dict = dict()
    class_dict = dict()
    
    for i in items:
        Items.append(i[0])
        weight_dict[i[0]] = i[2]
        cost_dict[i[0]] = i[3]
        earn_dict[i[0]] = i[4] - i[3]
        class_dict[i[0]] = i[1]
    
    Class_dict = defaultdict(list)
    for key, value in sorted(class_dict.iteritems()):
        Class_dict[value].append(key)
    
    # Create the 'prob' variable to contain the problem data
    prob = LpProblem("The PICKITEMS Problem", LpMaximize)
    # Two dictionary called 'x_vars' and 'y_vars' are created to contain the referenced Variables
    x_vars = LpVariable.dicts("",Items,0,1,cat=LpInteger)
    y_vars = LpVariable.dicts("#",range(N),0,1,cat=LpInteger)
    
    # The objection function is added to 'prob' first
    prob += lpSum([earn_dict[i]*x_vars[i] for i in Items]), "Total money we can earn in this file"
    
    # Constraints are added to 'prob'
    prob += lpSum([weight_dict[i]*x_vars[i] for i in Items]) <= P, "WeightsRequirement"
    prob += lpSum([cost_dict[i]*x_vars[i] for i in Items]) <= M, "CostRequirement"
    # the relations(constraint) between class and item (x and y)
    for num in range(C):
        for i in Class_dict[num]:
            prob += LpConstraint(x_vars[i]-y_vars[num] <= 0), ""
    # the relations for class constraints
    for constraint in constraints:
        prob += lpSum([y_vars[i] for i in constraint]) <= 1, ""
    # The problem is solved using PuLP's choice of Solver
    prob.solve()
    
    items_chosen = []
    for v in prob.variables():
        if v.varValue == 1 and v.name[0]!='#':
            items_chosen.append(v.name[1:])
    return items_chosen


"""
===============================================================================
  No need to change any code below this line.
===============================================================================
"""

def read_input(filename):
  """
  P: float
  M: float
  N: integer
  C: integer
  items: list of tuples
  constraints: list of sets
  """
  with open(filename) as f:
    P = float(f.readline())
    M = float(f.readline())
    N = int(f.readline())
    C = int(f.readline())
    items = []
    constraints = []
    for i in range(N):
      name, cls, weight, cost, val = f.readline().split(";")
      items.append((name, int(cls), float(weight), float(cost), float(val)))
    for i in range(C):
      constraint = set(eval(f.readline()))
      constraints.append(constraint)
  return P, M, N, C, items, constraints

def write_output(filename, items_chosen):
  with open(filename, "w") as f:
    for i in items_chosen:
      f.write("{0}\n".format(i))

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="PickItems solver.")
  parser.add_argument("input_file", type=str, help="____.in")
  parser.add_argument("output_file", type=str, help="____.out")
  args = parser.parse_args()

  P, M, N, C, items, constraints = read_input(args.input_file)
  items_chosen = solve(P, M, N, C, items, constraints)
  write_output(args.output_file, items_chosen)
