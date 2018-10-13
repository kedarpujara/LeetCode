public class four{
  public boolean isPowerOfFour(int num) {
    //System.out.println(((num)&(num-1)));
    //System.out.println(715827882&num);
    //return (  (num>0) && ( ((num)&(num-1)) == 0 ) && (715827882&num) == 0 );
    return (  (num>0) && (715827882&num) == 0 );
  }

  public static void main(String[] args) {
    four f = new four();
    System.out.println(f.isPowerOfFour(5));
  }
}
