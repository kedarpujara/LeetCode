import java.util.*;
class FindDuplicates {
  public List<Integer> findDuplicates(int[] nums) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    List<Integer> ar = new ArrayList<Integer>();
    for(int i = 0; i < nums.length; i++){
        if(map.containsKey(nums[i])){
            ar.add(nums[i]);
        } else {
            map.put(nums[i], 1);
        }
    }
    return ar;
  }

  public static void main(String[] args) {
    FindDuplicates fd = new FindDuplicates();
    int[] nums = {2,3,4,2};
    System.out.println(fd.findDuplicates(nums));
  }
}
