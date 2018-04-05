import java.util.*;

class JudgeRouteCircle {
  public boolean checkCircle(String moves){
    int x =0, y = 0;
    char[] move = moves.toCharArray();
    for(int i = 0; i < move.length; i++){
      if (move[i] == 'U')
        y++;
      else if(move[i] == 'D')
        y--;
      else if(move[i] == 'R')
        x++;
      else if(move[i]=='L')
        x--;
    }
    if(x==0 && y == 0) {
      return true;
    } else {
      return false;
    }


  }

  public static void main(String[] args) {
    String moves = "UD";
    JudgeRouteCircle jrc = new JudgeRouteCircle();
    System.out.println(jrc.checkCircle(moves));
  }
}
