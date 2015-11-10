// Using JAVA, answer the question below:
// Reverse the words in a given sentence.
// Words are always delimited by spaces. 
// For example if the given word is "reverse words of a sentence".
// The output will be "sentence a of words reverse"
class Main {

  public static void ReverseString(String str){
      
    String [] str_arr = str.split(" "); 
    for(int i = str_arr.length -1; i >= 0; i--) {
        System.out.print(str_arr[i]+" ");
    }

  }
  public static void main(String[] args) {
    ReverseString("hello world");
  }
}