class InsertionSort{
  public int[] insertionSort(int[] a){
    int n = 0;
    int curr = 1;
    int temp1 = 0;
    int temp2 = 0;
    for(int i = 1; i < a.length; i++){
      while(a[i-n] < a[i-n-1] && (i-n) > 1){
        temp1 = a[i-n];
        temp2 = a[i-n-1];
        a[i-n-1] = temp1;
        a[i-n] = temp2;
        if(i-n >= 0) n++;
        else break;
        // System.out.println(a[i-n]);
        // System.out.println(n);

      }
    }
    return a;


  }



  public static void main(String[] args) {
    InsertionSort is = new InsertionSort();
    int[] unsorted = {5,4,3,1,2};
    int[] sorted = is.insertionSort(unsorted);
    System.out.println(sorted[0]);
    System.out.println(sorted[1]);
    System.out.println(sorted[2]);
    System.out.println(sorted[3]);
    System.out.println(sorted[4]);
  }

}
