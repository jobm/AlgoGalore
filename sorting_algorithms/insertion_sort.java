class Main {
  public static void main(String[] args) {
      int [] arr = new int [] {65,31,2,1,9};
      insertsort(arr,arr.length);
      for(int i = 0;i < arr.length;i++){
           System.out.println(arr[i]);
      }
  }
  static void insertsort(int[] data, int n)
  {
      int i, j;
      for (i = 1; i < n; i++)
      {
          int item = data[i];
          int ins = 0;
          for (j = i - 1; j >= 0 && ins != 1; )
          {
              if (item < data[j])
              {
                  data[j + 1] = data[j];
                  j--;
                  data[j + 1] = item;
              }
              else ins = 1;

          }
      }
    }
}
