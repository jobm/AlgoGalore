import java.util.*;
 class Main {
     public static int adds_n(int num) {
         int sum = 0;
         for(int i = 1; i <= num; i++){
             sum += i;
         }
         return sum;
     } 
     public static void main(String[] args) {
         System.out.println("Enter the maximum number: ");
         Scanner scan = new Scanner(System.in);
         int s = scan.nextInt();
         System.out.println(adds_n(s)); 
  }
}