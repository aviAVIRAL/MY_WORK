# Painter’s Partition Problem
# Problem Statement: Given an array/list of length ‘N’, where the array/list represents the boards and each element of the given array/list represents the length of each board. Some ‘K’ numbers of painters are available to paint these boards. Consider that each unit of a board takes 1 unit of time to paint. You are supposed to return the area of the minimum time to get this job done of painting all the ‘N’ boards under the constraint that any painter will only paint the continuous sections of boards.

# Pre-requisite: BS-18. Allocate Books or Book Allocation | Hard Binary Search

# Examples
# Example 1:
# Input Format: N = 4, boards[] = {5, 5, 5, 5}, k = 2
# Result: 10
# Explanation: We can divide the boards into 2 equal-sized partitions, so each painter gets 10 units of the board and the total time taken is 10.

# Example 2:
# Input Format: N = 4, boards[] = {10, 20, 30, 40}, k = 2
# Result: 60
# Explanation: We can divide the first 3 boards for one painter and the last board for the second painter.

# We can allocate the boards to the painters in several ways but it is clearly said in the question that we have to allocate the boards in such a way that the painters can paint all the boards in the minimum possible time. The painters will work simultaneously.











