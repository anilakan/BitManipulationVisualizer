Bit Visualizer is a configurable package that displays bit operations happening in real time. 
A command-line interface, this tool aims to show students what is happening when a bit operation executes, at a low-level.
For example, if they are performing a shift, they will be able to see the bits moving, and interpret the final output as
both a bit vector and integer.

This package was developed to aid students taking Introduction to Computer Systems at Carnegie Mellon University, particularly
during Datalab. It can be used to debug puzzles and figure out if operations are doing what you intended, or simply see bit masks
at every stage of your solution to a puzzle, without you having to draw out all the bits at every stage.

Link to Deepnote: https://deepnote.com/workspace/S22-06682-8e2aa969-b312-4e88-82bb-e67f11508b8a/project/project-anilakan-a6a8e709-064a-45a5-8918-f0374a444bcf/
(Note: This is the second Deepnote I used for this project, the other one's terminal stopped working but is linked here: https://deepnote.com/workspace/S22-06682-8e2aa969-b312-4e88-82bb-e67f11508b8a/project/project-71b02ca7-7990-4b06-9d86-f1dee5e21fda/ )

1. Installing the Package 

Run the following command:

    pip install -e src

You should now have the 'bit_visualize' package. Inside src/bit_visualize, you'll find the script 'visualizer.py'. 
This is the runnable command. 

'bit_ops.py' implements each operation that the package is capable of. Currently, supported bit operations are 
<<, >> (arithmetic & logical), ~, and !. 

'variables.py' defines the GlobalVar class that manages user settings and stores variables the user is utilizing.
Functions that modify or parse commands to figure out what to run, and update variables, are also stored in this file.

'test_visualizer.py' is a file containing tests for the bit visualizer, with at least one test per operation.
Pytest can be used to run this file. 

2. Running the package

To run the visualizer, simply type 

    visualizer.py -b 32

into your command line. This runs the visualizer and stores all variables in 32-bit form. You can use 64-bit values
by instead running 

    visualizer.py -b 64

The '-b' flag sets the number of bits your variables will have. The only two options are 64 or 32, and any other
inputs will yield an error. 

You can set "rest time" with the -r flag. This is the speed at which the output of your operation will be displayed. 
By default, this is 0.2. If you tried to flip all the bits of a variable using the '~' operator, you would see one bit
flip every 0.2 seconds. The line:

    visualizer.py -b 32 -r 0

would run the visualizer with 32 bit values and zero rest time, so the output of an operation would be displayed
immediately after the computation is complete, all at once. 

The '-l' flag sets your new line preference. Whenever an operation is done, the package first displays the original value, 
and then displays the output. By default, the line preference is set to the value of '\r', so the bits of the output will
start to overwrite the original value. By setting the flag, you will change the line preference to '\n', so a new line 
will be created, allowing you to see both your original value and output value at the same time. 

    Without -l:
    >> var x = 0
    >> x = ~x
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 # output after x = ~x, halfway through being written over the initial value

    With -l:
    >> var x = 0
    >> x = ~x
        0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 # initial value 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1                                   # output after x = ~x, currently being printed on a new line


The '-s' flag signals that you want to interpret bits as a signed value. If you're using 32-bit values, for example, and
set the -s flag, then 0xFFFFFFFF would be interpreted as -1 instead of 4294967295. *Note: This feature is not yet implemented,
so setting the flag won't change the interpreted value. 

To run the visualizer with 64 bit values interpreted as signed values, 0.5 seconds of rest time during display,
and a new line seperating initial and output values, you would run the following command:

    visualzer.py -b 64 -r 0.5 -s -l

3. Command line operations
The main features this package allows are creating variables, updating variables with bit operations, displaying all saved variables,
and quitting. 

To create a new variable, enter 

    >> var <x> = <0> 

where <x> can be any letter of your choosing and <0> can be any value. The integer value you set the variable to can be
written in either binary or decimal form. To write the value as a binary form, simply write 'b' followed by your bit vector, as such:

    >> var y = b110100101

Make sure that you do not exceed the number of bits you selected upon startup (32 or 64).

Here are a few variations to update a variable:

    >> x = ~x # updates x with ~x
    >> y = x >> 2 # right shift x by 2, and update y with this new value. note that 'y' should have already been declared using var y = <0>,
                    or you'll get an error

Failure to write "<x> = " before your bit operation will result in an error.

To display all your saved variables, use

    >> display   # displays saved values as integers
    >> display b # displays in binary form

Your output will be printed to the terminal similar to this:

    x: 0
    y: 73
    z: 24

or for display b:

    a: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
    b: 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 
    c: 1 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 

To quit the program, use

    >> quit

Note that all command line operations are space sensitive, so typing

    >> var x= 0

will not work, as it is not equivalent to 

    >> var x = 0


4. Bit operations

At the beginning of any bitwise operation, you'll see the initial value in bits being printed,
your new output value being printed in bits, and then the output value interpreted as an integer.
For example, if you have the following sequence:

    >> var x = 32
    >> x = x >> 2
       0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
       0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0

       8
    >>
We currently support left-shift (<<), right shift (>>), bitwise not (~), and logical not (!).

a) << 

    Enter in command line:
        <x> = <x> << <y>
       Outputs x << y, where both x and y are saved variables in this run of the program. 
       Alternatively, you can write

       <x> = <x> << <2>
       where the second operator is now a decimal form integer of your choosing.
       The left shift is the only command where the output will print from right to left, so
       the shift can be visually shown. 

b) >>

    Enter in command line:
        <x> = <x> >> <y>
        or
        <x> = <x> >> <y> L
        Outputs x >> y, similar to the left shift operator above. You can also replace the second variable <y> with
        an integer. 

        If an L is placed at the end of the operation, a logical right shift will be performed. Instead of the most
        significant bit being copied in as the x is shifted to the right, 0s will be filled in. 


c) ~

    Enter in command line:
        <x> = ~<y>

        Outputs ~y, which flips each bit in y.

d) !

    Enter in command line:
        <x> = !<y>

        Outputs !y, which returns 1 if y == 0 and 0 if y != 0


5. Bugs and future extensions

Current known bugs:


    - Left shift: The command line cursor doesn't move as the bits are written from right to left, so
                  it might seem like bits aren't changing if they happen to be the same after the operation is done.
                  Although this isn't a bug, this is a little visually confusing since all the other commands have the
                  cursor hovering over the bit that is changing, assuming rest != 0.


    - The signed bit functionality isn't yet developed, so putting '-s' upon start up doesn't currently do anything.
    

    - Shift operators can have the second operator as an integer, but it must be written in decimal form, not binary.
      This is inconsistent with the ability to use decimal or binary interchangeably in the rest of the packet.


    - The __init__.py should be in the bit_visualize folder, but to make the pytest work upon upload to Github and also have the
      paths work out, I had to move it here. 

Future extensions:


    - Currently, you need to input each line upon each new run of the program. This isn't very convenient to run many
      trials successively, so I plan to write a script that can read the operations from a file and execute them successively.
      This would make steps such as saving variables much more efficient, and the user can continue working off the command line.

      
    - I want to implement more operations, such as +, &, |
