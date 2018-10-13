import  java.util.*;
class MinDeleteSum {
  public int minDelSum(String s1, String s2) {
    char[] c1 = s1.toCharArray();
    char[] c2 = s2.toCharArray();
    int cost1 = 0, cost2 = 0;

    int[][] dp = new int[c1.length+1][c2.length+1];

    for(int i = 0; i < c1.length; i++) {
      dp[i][0] = (int) c1[i];
      cost1 += (int) c1[i];
    }
    for(int i = 0; i < c2.length; i++) {
      dp[0][i] = (int) c2[i];
      cost2 += (int) c2[i];
    }
    // System.out.println(Arrays.toString(dp));
    int tempMin = 0;
    for(int i = 1; i <= c1.length; i++) {
      for(int j = 1; j <= c2.length; j++) {
        // System.out.println(dp[i-1][j-1]);
        if(dp[i][j] == dp[i-1][j-1]) {
          dp[i][j] = dp[i+1][j+1];
        } else {
          dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]);

        }


      }
    }
    return dp[s1.length()-1][s2.length()-1];

  }


  public static void main(String[] args) {
    MinDeleteSum mds = new MinDeleteSum();
    System.out.println(mds.minDelSum("delete", "leet"));
    // String st1 = "hello";
    // char[] c1 = st1.toCharArray();
    //
    // System.out.println((int) c1[0]);
    // System.out.println(st1.codePointAt(0));
  }

}
