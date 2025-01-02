# Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Reference https://leetcode.com/problems/two-sum/description/



## Solution
Examples: about the solution works

$$ x = target - n $$

nums = [2,7,11,15], target = 9

(1). 9 - 2 = 7

nums = [3,2,4], target = 6

(1). 6 - 3 = 3

(2). 6 - 2 = 4



That was my train of thought: I need to create a dictionary to store the result of the equation (target - num) and the index of the number. This result will help me complete the target value.

The time and space complexity of my solution is 𝑂(𝑛). This is because there is a single iteration through the list in the code, and for memory, I use a dictionary, which grows linearly with the number of elements in the list.