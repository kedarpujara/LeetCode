class three {
    public boolean isPowerOfThree(int n) {
        System.out.println(n==1);
        // if (n == 1){
        //     return true;
        // }
        //boolean isTrue = False;
        if (n % 3 == 0){
            n = n/3;
            isPowerOfThree(n);
        } else {
            System.out.println(n);
            if(n == 1){
              System.out.println("Here");
              return true;
            } else{
                return false;
            }

            // if(n == 1){
            //     return true;
            // } else {
            //     return false;
            // }
        }
    }
    public static void main(String[] args) {
      three t = new three();
      System.out.println(t.isPowerOfThree(9));
    }
}
