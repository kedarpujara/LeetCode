class HouseRobber{
  public int robApproach1(int[] nums){
    int maxSum = 0;
    int i = 0;
    // maxSum = Math.max(nums[0], nums[1]);
    // if(maxSum == nums[0]) i = 0;
    // else i = 1;

    int newSum = 0;
    int tempSum = 0;
    int j = 0;
    while(i < nums.length){
      if(i == 0) {
        tempSum = Math.max(nums[i], nums[i+1]);
        if(tempSum == nums[i+1]) j = 1;
      }
      // if(nums[j+2] == null || nums[j+3] == null) {
      //   return maxSum;
      // }

      newSum = Math.max(nums[j+2],nums[j+3]);
      if(newSum == nums[i+2]) j += 2;
      else j += 3;

      if(i != 0){
        maxSum = Math.max(nums[i-1] + nums[i+1], tempSum + newSum);
        if(maxSum == tempSum + newSum) i+= j;
        else i += 1;
      }

    }
    return maxSum;
  }



  public int rob(int[] nums){
    int[] dp = new int[nums.length];
    if(nums.length == 0) return 0;
    if(nums.length == 1) return nums[0];
    if(nums.length == 2) return Math.max(nums[0], nums[1]);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);
    for(int i = 2; i < nums.length; i++){
      dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
    }
    return dp[nums.length-1];
  }



  public static void main(String[] args) {
    HouseRobber hr = new HouseRobber();
    int[] test = {100,50,100,50,100};
    int[] test2 = {100,101,100,1,2};
    int[] test3 = {2,1,1,2};
    System.out.println(hr.rob(test3));
  }
}
