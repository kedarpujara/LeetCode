class ComplexNumberMultiplication{
  public String complexNumberMultiply(String a, String b){
    String[] string1 = a.split("\\+");
    String[] string2 = b.split("\\+");
    
    System.out.println(string1[1]);
    return "0";
  }

  public static void main(String[] args) {
    ComplexNumberMultiplication cnm = new ComplexNumberMultiplication();
    System.out.println(cnm.complexNumberMultiply("1+1i", "1+1i"));
  }
}
