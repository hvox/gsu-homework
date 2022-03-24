#!/usr/bin/env -S gap -q
# lab 2

# task 1
t := X(Rationals, "t");
task1 := (t-2)^5 + 4*(t-2)^4 + 4*(t-2)^3 - 8*(t-2)^2 - 32*(t-2) - 32;
Print("task1: ", task1, "\n");

# task 2
#  2α + 3β + γ = 6;
#  α + 2β - γ = 2;
# -3α -5β + γ = -7;
task2 := Determinant([[2, 1, -3], [3, 2, -5], [1, -1, 1]]);
task2r := [[2, 3, 1], [1, 2, -1], [-3, -5, 1]]^(-1) * [6, 2, -7];
Print("task2: ", task2r, "\n");

# task 3
x := X(Rationals, "x");
y := X(Rationals, "y");
task3 := [[0, 3], [2, 2]]^(-1) * [x, y];
Print("task3: ", task3, "\n");
