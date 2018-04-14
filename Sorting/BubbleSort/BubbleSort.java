class BubbleSort{

  public int[] bubbleSort(int[] a){

    int temp1 = 0;
    int temp2 = 0;
    for(int i = 0; i < a.length; i++){
      for(int j = 0; j < a.length-1; j++){
        if(a[j] > a[j+1]) {
          temp1 = a[j];
          temp2 = a[j+1];
          a[j] = temp2;
          a[j+1] = temp1;
        }
      }
    }

    return a;
  }

  public static void main(String[] args) {
    BubbleSort bs = new BubbleSort();
    int[] unsorted = {3,4,5,1,2};
    int[] sorted = bs.bubbleSort(unsorted);
    System.out.println(sorted[0]);
    System.out.println(sorted[1]);
    System.out.println(sorted[2]);
    System.out.println(sorted[3]);
    System.out.println(sorted[4]);

  }

}
