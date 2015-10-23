// Using java solve the problem below:
// Given an array of integers, find the maximum and minimum of this array.
import java.util.Arrays;
class Main {
    public static int [] Arr(int [] arr){
        int [] arr_min_max = new int []{};
        Arrays.sort(arr);
        arr_min_max = new int [] {arr[arr.length -1], arr[0]};
        return arr_min_max;
    }
  public static void main(String[] args) {
     
   
    for(int i = 0; i < Arr(new int[]{100,3,43,5,8}).length; i++){
         System.out.println(Arr(new int []{100,3,43,5,8})[i]);
    }
  }
}