import java.lang.Math;

class IsPrime {
  public boolean isPrime(int n){
    int sqrt = (int) Math.sqrt(n);
    for(int i = 2; i <= sqrt; i++){
      if( n % i == 0){
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    IsPrime ip = new IsPrime();
    System.out.println(ip.isPrime(18));
  }
}
