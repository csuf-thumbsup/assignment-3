# assignment-3

Given the following text file "data.txt". Write a program to copy the file into file "newdata.txt" by removing all comment lines (lines that begin with //), blank lines, extra spaces before and after each token (leave one space before and one after each token)

####"data.txt" file
    //declare variables
    int   num1,   nume2, num3 ,t;
    
    //initialize variables 
    num1  =3;  num2 =  5  ;
    	num3   =     7   ;
    //compute and display their total
    t=   num1  +  num2;//compute num1+num2
    t   =   t+num3; //compute new value for tl
    
    cout<<  t  ;
    
####"newdata.txt"
    int num1 , nume2 , num3 , t ;
    num1 = 3 ;
    num2 = 5 ;
    num3 = 7 ;
    t = num1 + num2 ;
    t = t + num3 ;
    cout<< t ;    
    
    

###Results from my attempt at Assignment 3;
    int num1 , nume2 , num3  , t ; 
    num1 =3 ; num2 = 5 ; 
    num3 = 7 ; 
    t=num1 + num2 ; 
    t = t + num3 ; 
    cout<< t ; 
    
There's some issues with spacing and having things be on a newline... but it sorta works.

Just to sorta explain what I did... 

I started off by reading in the textfile line by line into its own list.
    
    e.g ['//declare variables', 'int   num1,   nume2, num3 ,t;', '           ', '//initialize variables'] etc.

From there I then looped through each line and did some initial checks like if the line is a comment then skip over it or if it's empty then skip as well. Also I search the line if it contained an inline comment and removed that.
   
    e.g. 
    t=   num1  +  num2;//compute num1+num2
    becomes:
    t=   num1  +  num2;
    
Once I passed all the initial checks I split the line into a list by spaces (delimiter)
    
    e.g.
    t=   num1  +  num2;
    using: str_line = str_line[:str_line.index('//')]
    becomes:
    ['t=', 'num1', '+', 'num2;']
    
Next, I looped over that list from the line looking at each individual element one by one
This came with a simple check to see if it's length is 1 AND is a char terminal defined in [',', ';', '+', '-', '*', '/', '=']
If so then I just simply added a space to it

Else
I called reformat_text()

Which adds another space if there is no hidden terminal inside of it 
OR
Splits the given string by using the terminals as the delimiters. This is where RegEx comes into play.
    
    re.split('([-,;+*\/])', text_str)
That splits some text_str where a character matches from the following terminal list [',', ';', '+', '-', '*', '/', '='] 
    
    e.g.
    re.split('([-,;+*\/])', num2;)
    becomes:
    ['num2', ';', '']  
    
Then i joined that split_text_str back together with spaces following each item
    
    Goes from ['num2', ';', '']  
    using: ' '.join(split_text_str)
    becomes: num2 ; 
    # note that there is a space after the semicolon it just cant be seen.
    
Then it loops back and repeats the whole process... Hopefully that helps you guys figure out how to do it somehow.
    

