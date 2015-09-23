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
