<<<<<<< HEAD
import java.util.*;
public class Main{
    public static void GetUserInput(){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a string of words");
        String s = input.nextLine();
        if(s == null || s.length() ==0){
            return;
        }
        System.out.println(Capitalize(s.trim().toLowerCase()));
    }
    public static String Capitalize(String input){
        String [] caps = input.split(" ");
        String space = " ";
        String capitalize = "";
        String formed = " ";
        for(int i = 0;i < caps.length; i++){
            capitalize = caps[i].substring(0,1).toUpperCase()+caps[i].substring(1,caps[i].length())+space;
            formed += capitalize;
        }
        return formed;
    }
    public static void main(String [] args){
        GetUserInput();
    }
}
=======
// Using java, have the function capitalize(str) take the str parameter being passed and capitalize
// the first letter of each word. Words will be separated by only one space.
// the scanner object should be in the main method, from where we are going to call our function for testing
// it should take string input from a user
>>>>>>> 7cccf75f5eeb839e84d646aac854e19e5f5c68c8
