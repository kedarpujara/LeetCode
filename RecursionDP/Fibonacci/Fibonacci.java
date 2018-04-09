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

  public int iterDpFib(int n){
    int[] memo = new int[n];

    memo[0] = 0;
    memo[1] = 1;
    for(int i = 2; i < n; i++){
      memo[i] = memo[i-1] + memo[i-2];
    }
    return memo[n-1] + memo[n-2];

  }


  public static void main(String[] args) {
    Fibonacci fib = new Fibonacci();
    //System.out.println(fib.FibRec(50));
    System.out.println(fib.fibMemStart(30));
    System.out.println(fib.iterDpFib(30));
  }
}
