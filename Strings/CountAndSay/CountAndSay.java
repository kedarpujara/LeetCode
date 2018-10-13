class CountAndSay{
  public String countAndSay(int n){
    Map<Character, String> count = new HashMap<Character, String>();
    count.put('1',"one");
    count.put('2', "two");

    String num = Integer.toString(n);
    char[] numChar = num.toCharArray();
    int counter = 0;
    for(int i = 1; i < numChar.length; i++){
      if(numChar[i] == numChar[i-1]){
        counter++;
      } else{

      }
    }
  }

  public static void main(String[] args) {
    CountAndSay cas = new CountAndSay();
    System.out.println(cas.countAndSay(5));
  }
}
