// Input: "Let's take LeetCode contest"
// Output: "s'teL ekat edoCteeL tsetnoc"

class ReverseWords {

  public String reverseWords(String s) {
    String[] split = s.split("\\s+");
    for(int i = 0; i < split.length; i++){
      split[i] = reverseStr(split[i]);
    }

    String ret = String.join(" ", split);
    System.out.println(ret);
    return ret;
  }

  public String reverseStr(String s){
    char[] reverse = s.toCharArray();
    char[] temp = new char[reverse.length];
    int j = 0;
    for(int i = reverse.length - 1; i >= 0; i--){
      temp[j] = reverse[i];
      j++;
    }
    String retStr = new String(temp);
    return retStr;
  }

  public static void main(String[] args) {
    ReverseWords rw = new ReverseWords();
    rw.reverseWords("hello my name is kedar");

  }
}
