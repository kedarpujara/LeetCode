class Fibonacci {

  //Return nth fibonacci number
  public int FibRec(int n){
    if(n == 0) return 0;
    if(n == 1) return 1;

    return FibRec(n-1) + FibRec(n-2);
  }


  /* Using memoization */
  public int fibMemStart(int n) {
    return FibMemoization(n, new int[n+1]);
  }

  public int FibMemoization(int n, int[] memo){
    if(n == 0 || n == 1) return n;

    if(memo[n] == 0) {
      return FibMemoization(n-1, memo) + FibMemoization(n-2, memo);
    }

    return memo[n];
  }

  public static void main(String[] args) {
    Fibonacci fib = new Fibonacci();
    //System.out.println(fib.FibRec(50));
    System.out.println(fib.fibMemStart(6));
  }
}
