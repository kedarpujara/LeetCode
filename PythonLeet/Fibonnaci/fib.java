public class fib {

	/*** ALGORITHM 1 ***/
	//In the order of 2^n

	public void printFib(int n){
		for(int i=1; i <= n; i++){
			System.out.println(i + ": " + fib(i));
		}
	}

	public int fib(int n) {
		if(n==0)
			return 0;
		else if(n==1)
			return 1;
		else
			return fib(n-1) + fib(n-2);
	}


	/***ALGORITHM 2 ***/


	public void printAllFib(int n){
		int[] memo = new int[n+1];
		for(int i = 0; i < memo.length; i++) {
			System.out.println(i + ": " + fib(i, memo));
		}
	}

	public int fib(int n, int[] memo){
		if(n==0) 
			return 0;
		else if(n==1)
			return 1;
		else
			memo[n] = memo[n-1] + memo[n-2];

		return memo[n];
	}



	public static void main(String[] args){
		fib fibon = new fib();
		System.out.println(fibon.fib(8));
		//fibon.
	}	

}

//Runtime of fib 

/* 
 * printFib goes in the order of n. but it also calls fib in its loop
 * fib runs in the order of 2^n, which is very bad 
 */