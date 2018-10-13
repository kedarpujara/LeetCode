class MaxSumSubarray {

  public int maxSumSubarray(int[] nums){
    int n = nums.length;
    int sum = 0;
    int ans = nums[0];

    ans = 0;
    for(int i = 0; i< n; i++){
        if(nums[i] + sum > 0){
          sum += nums[i];
        } else {
          sum = 0;
        }

        ans = Math.max(ans, sum);
    }
    return ans;
  }

  public static void main(String[] args) {
    MaxSumSubarray mss = new MaxSumSubarray();
    int[] a = {-5, -1, 6, -8};
    System.out.println(mss.maxSumSubarray(a));
  }

}
