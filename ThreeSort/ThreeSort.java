// THREESORT
// LANGUAGE: JAVA

// Create a ThreeSort class with a threeSort method and a main method.
// The threeSort method should contain the algorithm and the main method
// should be used for testing your algorithm. To make that easier, make the
// threeSort method static.

// Given three numbers as input, find the min, middle and max of the three.
// Return an array of the numbers in ascending order.
// Hint: to easily see your output, import java.util.Arrays
// and use the Arrays.toString(array) method to convert the Array to a string 
// and then log it using System.out.println();

// Example:
// ThreeSort.threeSort(9,4,6); // [4,6,9]
// ThreeSort.threeSort(3,2,1); // [1,2,3]

import java.util.Arrays;
class Main {
    public static int[] TreeSort(int a,int b,int c){
        int [] arr = new int [] {a,b,c};
        Arrays.sort(arr);
        return arr;
    }
  public static void main(String[] args) {
      
      for(int i = 0; i < Main.TreeSort(5,2,4).length; i++){
          System.out.println(Main.TreeSort(5,2,4)[i]);
      }
      
  }
}
