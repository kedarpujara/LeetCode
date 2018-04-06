import java.util.*;


class ArrayPartition {
  public int arrayPairSum(int[] nums){
    Arrays.sort(nums);
    int minSum = 0;
    int i = 0;
    while(i < nums.length){
      minSum += Math.min(nums[i], nums[i+1]);

      if((i+1) == nums.length-1){
        return minSum;
      } else i = i+2;
    }
    return minSum;
  }

  public static void main(String[] args) {
    ArrayPartition ap = new ArrayPartition();
    int[] nums = {1,5,3,6};
    System.out.println(ap.arrayPairSum(nums));
  }
}
