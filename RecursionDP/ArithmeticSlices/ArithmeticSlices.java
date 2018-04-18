import java.util.*;
class ArithmeticSlices {
  public int arithSlice(int[] A){
    int[] diff = new int[A.length-1];
    for(int i = 1; i < A.length; i++){
      diff[i-1] = A[i] - A[i-1];
    }
    int counter = 1;
    int j = 1;
    int numSlice = 0;
    int length = diff.length;
    System.out.println(length);
    for(int i = 1; i < diff.length; i++){
      while(diff[j] == diff[j-1] && j < length){
        j++;
        counter++;
      }
      if(counter == 1) {
        counter = 0;
        i += j-1;
        System.out.println(i);
        j = i;

      } else if (counter >= 2) {
        System.out.println(numSlices(counter));
        numSlice += numSlices(counter);
        i += j-1;
        System.out.println(i);
        j = i;
      }
    }
    return numSlice;
  }

  public int numSlices(int num){
    int total = 0;
    for(int i = num; i>=3; i-- ){
      total += num-i+1;
    }
    return total;
  }

public static void main(String[] args) {
  ArithmeticSlices as = new ArithmeticSlices();
  int[] A = {5,1,2,3,4,6,8,9,10};
  int[] B = {1,1,1,1};
  System.out.println(as.arithSlice(B));
}

}
