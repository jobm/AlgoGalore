class Main {
public static int[] BubbleSort(int [] data){
        int temp = 0;
        boolean flag = true;
        for(int count = 0; count < data.length ; count++){
            flag = true;
            for(int sort = 0; sort < data.length - 1; sort++){
                if(data[sort] > data[sort + 1]){
                    temp = data[sort + 1];
                    data[sort + 1] = data[sort];
                    data[sort] = temp;
                    flag = false;
                }
            }
            if(flag){break;}
        }
        return data;
    }
  public static void main(String[] args) {
      int [] beer = new int [] {5,6,8,3,1};
      for(int i = 0; i < BubbleSort(beer).length; i++){
          System.out.println(BubbleSort(beer)[i]);
      }

  }
}
