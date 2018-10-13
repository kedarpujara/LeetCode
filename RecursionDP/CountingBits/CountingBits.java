import java.util.*;


class CountingBits{
  public int[] countBits(int num){
    int[] ret = new int[num+1];
    for(int i = 0; i <= num; i++){
      ret[i] = binaryNum(i);
    }
    return ret;
  }

  public int randomTest(int[] num){
  	int x = 0;
  	for(int i = 0; i < num.length; i++){
  		if(num[i] >= 6) {
  			i += 1;
  		} else {
  			x += num[i];
  		}
  		System.out.println(x);
  		System.out.println(i);
  		System.out.println("");
  	}
  	return x;
  }


  public int binaryNum(int num){
    String bi = Integer.toBinaryString(num);
    char[] biChar = bi.toCharArray();
    int counter = 0;
    for(int i = 0; i < biChar.length; i++){
      if(biChar[i] == '1') counter++;
    }
    return counter;
  }

  // public int[] countingBitsDP(int num) {
  //   int[] dp = new int[num+1];
  //   int p = 1;
  // }


  public static void main(String[] args) {
    CountingBits cb = new CountingBits();
    int[] num = {1,5,3,7,3,6,2};
    System.out.println(cb.randomTest(num));

    // int[] ar = cb.countBits(8);
    // System.out.println(Arrays.toString(ar));

    // int pow = 1;
    // pow <<= 1;
    // pow <<= 1;
    // pow <<= 1;
    // System.out.println("pow: " + pow);
    // int num = 15/2;
    // System.out.println(num);
  }
}
