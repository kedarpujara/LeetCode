import java.util.*;

public class twosum {

	public static int[] twoSum(int[] nums, int target) {
		int[] returNum = new int[2];
		returNum[0] = -1;
		returNum[1] = -1;
		Map<Integer, Integer> ind = new HashMap<Integer, Integer>();

		for(int i = 0; i < nums.length; i++) {
			if(ind.containsKey(nums[i])) {
				returNum[0] = ind.get(nums[i]) + 1;
				returNum[1] = i + 1;
				break;
			}
			else {
				ind.put(target-nums[i], i);
			}
		}
		System.out.println(returNum);
		return returNum;

	}

	public static void main(String[] args) {
		int[] nums = {3,2,1,4,6};
		int target = 10; 
		twoSum(nums, target);
		//System.out.println(ret);
		
	}
}

//iterate through the map and see if any of the keys are present 
//in the initial integer array 

//if it is present, return the index in the dictionary, in addition to the index it is present in the array 
