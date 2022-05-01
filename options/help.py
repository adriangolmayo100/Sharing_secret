def show():
    print("""
HELP MANUAL    
    
This application uses the Shamir algorithm to implement the secret sharing scheme. This consists that 
having a sharing secret number S, by using an interpolation algorithm, in this case the Lagrange algorithm, 
it can be retrieved by using a series of keys of size greater than a set limit. This is very useful for storing 
numeric keys, stock market values, etc.... 

The mode of use is very simple. When running the application a main menus will be executed. This menus will show the 
main functions of the application, plus settings and a help manual. The options offered are: 

    -Generate a sharing secret: This feature allows the user to create a sharing secret, for this the user will be 
    asked for the sharing secret, the number of people with whom he wants to share it and the minimum number of 
    people to extract this sharing secret. Then, the algorithm will calculate a polynomial that fits the conditions 
    provided and will return a key for each person. Such key is the one that the person will have to enter to be able 
    to recover the sharing secret. 

    -Recovering a sharing secret: This is the opposite option to the previous one, in which, first of all, 
    a number of people will be asked for their respective keys. If the number of people is equal or greater than the 
    number indicated as minimum number of people, and they introduce their passwords correctly, the sharing secret 
    will be shown. Otherwise, the sharing secret will not be displayed correctly and the program will not indicate 
    that the output is wrong because the program cannot store the sharing secret numbers. 

    -Settings: Allows you to change two options using a setting menu, the default way of displaying the keys is 
    shown on the screen but the program allows you to enter the e-mail addresses of the members and send them the 
    keys for more security. On the other hand, it allows you to choose how to enter the sharing secret, you can 
    either type in the predefined option or read the number from the first line of a file for more security. 

    -Help: Shows the user the application's help manual.
          """""
          )
