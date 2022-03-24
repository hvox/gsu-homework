#!/usr/bin/env -S gap -q
# lab 2

# task 1
t := X(Rationals, "t");
task1 := (t-2)^5 + 4*(t-2)^4 + 4*(t-2)^3 - 8*(t-2)^2 - 32*(t-2) - 32;
Print("task1: ", task1, "\n");
