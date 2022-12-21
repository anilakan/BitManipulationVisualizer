Project Proposal:
This project aims to aid engineering, particularly in a classroom setting. As a TA for Intro to Computer Systems, 
I’ve seen that students often have a hard time visualizing bitwise operations when completing Datalab. Solving the puzzles with a series of bitwise operations could be better understood/debugged 
if students could actually see what each step they write is doing.


I would like to make a package that provides this visualization in a command line style. 
The student would be prompted to select a few parameters, such as the length of the number, and the arguments you want to take in. Then, the student can type out an operation on an argument (one operation per line) 
and when they click enter, a pop up will show the bits moving. As an example, suppose a student is working on an implementation for trueThreeFourths, which takes in long x and is supposed to return 3/4 of x. 


The command line would ask for the length (64), number of args (1) and the arg (suppose b0010). You could then write the following:
    >> div_4 = x >> 2;
    < animation pops up that shows 0010 shifting over to become 0000 , div_4 saved as a variable>
    >> mult_32 = (x >> 1);
    < similarly to above >
    >> mult_32 += div_4;
    < shows div_4 and mult_32 being added together, bitwise, updates mult_32 >
    (.. and so on for the rest of the steps of this puzzle. Bit masks could also be saved and visualized 
    when used with the arguments.) 


With this integration, you’d be able to see the logical right shifts, 
as well as how bitwise adds are working if there is overflow, etc. While doing this lab myself, I found it hard to debug without physically drawing 
every single step, so I think this package would be helpful to students. It’s centered around use in Datalab, but could be used for any scenario in which you are trying to use bitwise logic 
and want to see what is actually happening to the bits.
It would also be nice if this could be integrated within a python function trueThreefourths itself, so that running the function would also display the visuals for each step until you click next/ enter.
I would essentially write an animation for each bitwise operation, such as >>, <<, |, &, ^.
Once I’m able to figure out animations, I should be able to reuse a lot of the code, and then it shouldn’t take more than a few hours.


 