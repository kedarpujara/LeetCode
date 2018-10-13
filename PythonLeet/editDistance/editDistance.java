import static java.lang.Math.*;

public class editDistance {
	public int editDistanceDP(String s1, String s2) {
		int[][] solution = new int[s1.length() +1][s2.length()+1];

		//base cases 
		for(int i = 0; i < s2.length(); i++)
			solution[0][i] = i;

		for(int i = 0; i < s1.length(); i++)
			solution[i][0] = i;

		int m = s1.length();
		int n = s2.length();

		//Bottom up
		for(int i = 1; i <= m; i++) {
			for(int j = 1; j <= n; j++) {

				if(s1.charAt(i-1) == s2.charAt(j-1))  //If last characters are matching, then advnance 
					solution[i][j] = solution[i-1][j-1];				
				else {
					solution[i][j] = 1 + Math.min(solution[i][j-1], //insert 
													Math.min(solution [i-1][j],//remove
													solution[i-1][j-1]));//replace)
				}
			}
		}

	return solution[s1.length()][s2.length()];
	}


	public static void main(String[] args) {
		editDistance ed = new editDistance();
		//answer1 = ed.editDistanceDP("Hello", "Hello!");
		System.out.println("Minimum Edit Distance: " + ed.editDistanceDP("hello", "Hello there!"));
	}
}