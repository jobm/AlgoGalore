class Main {
   public static int GetFibbo(int n){
   int f_num = 0,s_num = 1,result = 0;
   if(n == 0)return 0;
   if(n == 1) return 1;
   for(int i = 2; i <= n; i++){
       result = f_num + s_num;
       f_num = s_num;
       s_num = result;
   }
   return result;
}
 public static void main(String[] args) {
   for(int i = 0; i < 10; i++){
       System.out.println(GetFibbo(i));
   }
 }
}