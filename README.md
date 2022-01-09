# Stage 1/5: Data collection
#### Description
We will start by implementing the flowchart below. Copy the messages carefully and assign them to the program variables. It makes no difference whether you make a list or each message is a separate variable. The appropriate messages must be displayed according to the flowchart.

![](https://ucarecdn.com/b1770719-2eea-4389-b126-9fbd2edf8d96/)

#### Objectives
Implement the flowchart above. Please, follow our recommendations:

* The variable `calc` should have the following format: `x operation y`. For 
example: `2 + 3`, `2 + g` or `3.1 r 5`;
* The variables `x` and `y` must be of the ``float`` or ``int`` type. The oper variable 
  is a one-character string. Check whether the passed values have proper types. The delimiter must be a dot;
* Don't use the built-in `eval()` function to calculate from a string;
* Copy the messages below carefully. The tests will check if the correct 
  message appears in the correct order. Please, do not add extra lines or characters.
```
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
```
#### Example
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

#### Example 1:
```
Enter an equation
> 2 + m
Do you even know what numbers are? Stay focused!
Enter an equation
> 3 n 3
Yes ... an interesting math operation. You've slept through all classes, haven't you?
Enter the equation
> m - 2
Do you know what the numbers are? Stay focused!
Enter an equation
> 4.7 * 5.2
```
# Stage 2/5: First calculations
#### Description
In this stage, we will continue with the flowchart. Note that the blocks from the previous stage are in red. Be careful; some flows can work differently.
![](https://ucarecdn.com/14a82832-1487-4df0-8e1c-1893247d5193/)

#### Objectives
Implement the flowchart above. While doing it, please, follow our recommendations:

* Don't use the built-in functions to calculate from a string;
* The `result` variable must be of the `float` type;
* Copy the message. The tests will check if the correct message appears in 
  the correct order. So don't add extra lines or characters: `msg_3 = "Yeah... division by zero. Smart move..."`
#### Examples
The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

#### Example 1:

```
Enter an equation
> 2 + m
Do you even know what numbers are? Stay focused!
Enter an equation
> 3 n 3
Yes ... an interesting math operation. You've slept through all classes, haven't you?
Enter an equation
> 4 / 0
Yeah... division by zero. Smart move...
Enter an equation
> 4 * 5.2
20.8
```

#### Example 2:
```
Enter an equation
> 411 - 211
200.0
```

# Stage 3/5: Total recall
#### Description
Take a look at the upgraded flowchart. As before, the old blocks are red-colored. Be careful; some flows can now work differently.

![](https://ucarecdn.com/4a899d94-c524-48f1-8bfe-04ea9139172b/)

#### Objectives
To complete this stage, you need to implement the flowchart above. While doing it, please, follow our recommendations below:

* Don't use the built-in function `eval()` to calculate from a string;
* The `memory` variable must be of a float type;
* There are no tests when `M` is negative. For example, there will be no test 
  input like this: `-M + 6`;
* Copy two messages. The tests will check if the correct message appears in 
  the correct order. Don't add extra lines or characters.
```
msg_4 = "Do you want to store the result? (y / n):" 

msg_5 = "Do you want to continue calculations? (y / n):"
```
#### Example
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.

#### Example 1:
```
Enter an equation
> 3 + 3
6
Do you want to store the result? (y / n):
>y
Do you want to continue calculations? (y / n):
>y
> 5 + M
11
Do you want to store the result? (y / n):
>y
Do you want to continue calculations? (y / n):
>n
```
