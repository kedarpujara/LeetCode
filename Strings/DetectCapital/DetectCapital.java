class DetectCapital {

  public boolean detectCapital(String word){
    char[] cap = word.toCharArray();
    boolean allCaps = false;
    boolean lowercase = false;

    if(cap.length == 1) return true;

    if(Character.isUpperCase(cap[0]) == false){
      lowercase = true;
    }

    if (lowercase == true) {
      for(int i = 1; i < cap.length; i++){
        if(Character.isUpperCase(cap[i]) == true) {
          return false;
        }
      }
    }

    if (lowercase == false) {
      allCaps = Character.isUpperCase(cap[1]);
    }

    if(cap.length > 2) {
      for(int i = 2; i < cap.length; i++){
        if(allCaps){
          if(Character.isUpperCase(cap[i]) == false){
            return false;
          }
        } else if(Character.isUpperCase(cap[i]) == true) {
          return false;
        }
      }
    }
    return true;

  }

  public static void main(String[] args) {
    DetectCapital dc = new DetectCapital();
    System.out.println(dc.detectCapital("USaS"));
  }
}



// First, check if first case is lowercase or uppercase
// If lowercase, make sure the rest is lowercase
// If uppercase, then check if all caps
