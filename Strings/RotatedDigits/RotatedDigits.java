// Example:
// Input: 10
// Output: 4
// Explanation:
// There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
// Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

//Unfinished
import java.util.stream.IntStream;
import java.util.stream.LongStream;

class RotatedDigits {
  public int rotatedDigits(int N){
    int[] good = {2,5,6,9};
    int counter = 0;
    for(int i = 1; i <= N; i++){
      if(contains(good, i)) counter++;
    }

    return counter;
  }


  public static boolean contains(int[] arr, int item) {
   for (int n : arr) {
      if (item == n) {
         return true;
      }
   }
   return false;
  }

  public static void main(String[] args) {
    RotatedDigits rd = new RotatedDigits();
    System.out.println(rd.rotatedDigits(4));
  }
}
