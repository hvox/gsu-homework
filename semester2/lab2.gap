#!/usr/bin/env -S gap -q
# lab 2

# task 1
t := X(Rationals, "t");
x := t - 1;
task1 := x^5 + 4*x^4 + 4*x^3 - 8*x^2 - 32*x - 32;
Print("task1: ", task1, "\n");

# task 2
#  2α + 3β + γ = 6;
#  α + 2β - γ = 2;
# -3α -5β + γ = -7;
task2 := Determinant([[2, 1, -3], [3, 2, -5], [1, -1, 1]]);
task2r := [[2, 3, 1], [1, 2, -1], [-3, -5, 1]]^(-1) * [6, 2, -7];
Print("task2: ", task2r, "\n");

# task 3
task3 := [[0, 3], [2, 2]]^(-1) * [-5, 4];
Print("task3: ", task3, "\n");

# task 4
task4 := [
	[1, 2, 3, -1],
	[2, 3, 4, 4],
	[3, 4, 6, 7],
	[2, 3, 1, 9]
] ^ (-1) * [-1, 1, 2, -1];
Print("task4: ", task4, "\n");

# task 5
task5 := [[1, 4, 1, 2], [2, 7, -2, 0], [-1, 3, 0, -1]];
TriangulizeMat(task5);
Print("task5: ", task5, "\n");

# task 7
task7a := [[1,0,2], [3,-1,4], [2,-2,1]] * [[1,2,1],[2,3,3],[3,8,2]]^(-1);
task7b := [[1,2,1],[2,3,3],[3,8,2]] * [[1,0,2], [3,-1,4], [2,-2,1]]^(-1);
Print("task7a: ", task7a, "\n");
Print("task7b: ", task7b, "\n");
Print("c in E: ", [2, 0, 1] * [[1,2,1],[2,3,3],[3,8,2]]^(-1) , "\n");
Print("x in A: ", [1, -1, 2] * task7b , "\n");

# task 8
task8a := [[-1,2,3],[2,0,1],[-2,2,2]];
Print("task8a: ", task8a, "\n");
Print("task8r: ", task8a^(-1), "\n");
Print("task8v: ", [-3, 2, 0] * task8a^(-1), "\n");

x := X(Rationals, "x");
y := X(Rationals, "y");
