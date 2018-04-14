class RangeSumQuery {
  private int[] data;

  public RangeSumQuery(int[] nums){
    data = nums;
  }

  public int sumRange(int i, int j){

    int a = 0;
    int sum = 0;
    for(a = i; a <= j; a++){
      sum += data[a];
    }
    return sum;
  }

  public static void main(String[] args) {
    int[] nums = {3,2,-1};
    RangeSumQuery rsq = new RangeSumQuery(nums);
    System.out.println(rsq.sumRange(0,1));
  }
}
