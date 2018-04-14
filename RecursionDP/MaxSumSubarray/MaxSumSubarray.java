class MaxSumSubarray {

  public int maxSumSubarray(int[] nums){
    int n = nums.length;
    int sum = 0;
    int ans = nums[0];
    //Check if all negative
    // for(int i = 1; i < n; i++){
    //   ans = Math.max(ans, nums[i]);
    // }
    //
    // if(ans < 0){
    //   return ans;
    // }

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
    int[] a = {-2, -5, -1, -8};
    System.out.println(mss.maxSumSubarray(a));
  }

}
