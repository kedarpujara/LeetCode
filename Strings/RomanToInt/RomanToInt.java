import java.util.*;
class RomanToInt {
  public int romanToInt(String s){
    Map<Character, Integer> roman = new HashMap<Character, Integer>();
    roman.put('I', 1);
    roman.put('V', 5);
    roman.put('X', 10);
    roman.put('L', 50);
    roman.put('C', 100);
    roman.put('D', 500);
    roman.put('M', 1000);

    int totalValue = 0;

    int currVal = 0;
    char[] convert = s.toCharArray();
    for(int i = 0; i<convert.length; i++){
      currVal = roman.get(convert[i]);
      if(i == convert.length-1){
        return totalValue += currVal;
      }
      if(currVal == 1 && convert[i+1] == 'V'){
        totalValue += 4;
        i++;
      } else if (currVal == 1 && convert[i+1] == 'X'){
        totalValue += 9;
        i++;
      } else if (currVal == 10 && convert[i+1] == 'L'){
        totalValue += 40;
        i++;
      } else if (currVal == 10 && convert[i+1] == 'C'){
        totalValue += 90;
        i++;
      } else if (currVal == 100 && convert[i+1] == 'D'){
        totalValue += 400;
        i++;
      } else if (currVal == 100 && convert[i+1] == 'M'){
        totalValue += 900;
        i++;
      } else {
        totalValue += currVal;
      }
    }
    return totalValue;
  }



  public static void main(String[] args) {
    RomanToInt rti = new RomanToInt();
    System.out.println(rti.romanToInt("XIX"));
  }
}

/* RULES
I comes before V or X, subtract 1
X comes before L or C, subtract 10
if C comes before D or M, subtact 100
*/
