class ReverseString {
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
    ReverseString rs = new ReverseString();
    System.out.println(rs.reverseStr("kedar"));
  }
}
