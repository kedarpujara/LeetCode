public class CoinChange {

	public int minChange(int[] v, int amount) {

		int[][] solution = new int[v.length + 1][amount+1];

		if(amount == 0)
			return 1;

		for(int i = 0; i <= v.length; i++)
			solution[i][0] = i;

		for(int i = 0; i <= amount; i++)
			solution[0][i] = i;

		for(int i = 0; i < v.length; i++) {
			for(int j = 0; j < v.length; j++) {
				if(v[i-1] <= j) {
					solution[i][j] = solution[i-1][j] + solution[i][j - v[i-1]];
				} else {
					solution[i][j] = solution[i-1][j];
				}
			}
		}
	return solution[v.length][amount];
	}

	public static void main(String[] args) {

		int amount = 5;
		int[] v = {1,2,3};
		CoinChange cc = new CoinChange();
		System.out.println(cc.minChange(v, amount));

	}


}