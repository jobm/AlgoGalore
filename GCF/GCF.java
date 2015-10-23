// Using java, have the function divide(num1,num2)
// take both parameters being passed and return the Greatest Common Factor.
// That is, return the greatest number that evenly goes into both numbers with no remainder.
// For example: 20 and 10 both are divisible by 1, 2, 5 and 10 so the output should be 10.
// The range for both parameters will be from 1 to 10^3.
class Main {
  public static int gcf(int a,int b){      
      int small = 0, big = 0, gcd = 0;
      if(a > b){
         big = a; small = b;
      }
      else{
          small = a; big = b;
      }
      if(big % small == 0){
          gcd = small;
      }
      for(int i = small;i > 0; i--){
          if(big % i == 0 && small % i == 0){
              gcd = i; break;
          }
      }
      return gcd;
  }
  public static void main(String[] args) {
    System.out.println(gcf(8,12));
  }
}
