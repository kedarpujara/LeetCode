import java.util.*;


class CountingBits{
  public int[] countBits(int num){
    int[] ret = new int[num+1];
    for(int i = 0; i <= num; i++){
      ret[i] = binaryNum(i);
    }
    return ret;
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

  public static void main(String[] args) {
    CountingBits cb = new CountingBits();
    int[] ar = cb.countBits(8);
    System.out.println(Arrays.toString(ar));
    // int num = 15/2;
    // System.out.println(num);
  }
}
