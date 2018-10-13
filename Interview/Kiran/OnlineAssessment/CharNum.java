import java.util.*;

class CharNum {
  public void numStrings(String num) {
    Map<String, String> alphabet = MakeAlphabetMap();

    Map<String, String> possib = new HashMap<String, String>();

    ArrayList<String> ar = new ArrayList<String>();
    String curr = "";
    if(num.length() == 0) {
        possib.put("","");
        return;
    } else if(num.length() >= 1) {
      curr = Character.toString(num.charAt(0));
      curr = alphabet.get(curr);
      System.out.println(curr);
      possib.put("", "");
      possib.put("1", curr);
    }



    for(int i = 2; i < num.length(); i++){
      curr = Character.toString(num.charAt(i));
      curr = (String) curr;
      // possibilities.put(curr, )
    }


  }


  public Map<String, String> MakeAlphabetMap(){
    Map<String, String> alphabet = new HashMap<String, String>();
    alphabet.put("1", "a");
    alphabet.put("2", "b");
    alphabet.put("3", "c");
    alphabet.put("4", "d");
    alphabet.put("5", "e");
    alphabet.put("6", "f");
    alphabet.put("7", "g");
    alphabet.put("8", "h");
    alphabet.put("9", "i");
    alphabet.put("10", "j");
    alphabet.put("11", "k");
    alphabet.put("12", "l");
    alphabet.put("13", "m");
    alphabet.put("14", "n");
    alphabet.put("15", "o");
    alphabet.put("16", "p");
    alphabet.put("17", "q");
    alphabet.put("18", "r");
    alphabet.put("19", "s");
    alphabet.put("20", "t");
    alphabet.put("21", "u");
    alphabet.put("22", "v");
    alphabet.put("23", "w");
    alphabet.put("24", "x");
    alphabet.put("25", "y");
    alphabet.put("26", "z");

    return alphabet;
  }


  public static void main(String[] args) {
    CharNum cm = new CharNum();
    String num = "3";
    cm.numStrings(num);

  }
}
