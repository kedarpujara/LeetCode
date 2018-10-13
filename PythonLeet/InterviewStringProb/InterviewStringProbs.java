public class InterviewStringProbs {


	public boolean isPalindrome(String pal) {
		if (pal == null) {
			System.out.println("Null value");
			return false;
		}
		if (pal.length() == 0 || pal.length() == 1) {
			return true;
		}
		if(pal.charAt(0) == pal.charAt(pal.length()-1)) {
			return isPalindrome(pal.substring(1, pal.length()-1));
		}
		return false;
	}

	public int reverseInt(int original) {
		int reverse = 0;
		int remainder; 
		while (original != 0) {
			remainder = original  % 10;
			reverse = reverse*10 + remainder;
			original = original/10;
		}
		return reverse;
	}



	public static void main(String[] args) {
		InterviewStringProbs iv = new InterviewStringProbs();
		System.out.println(iv.isPalindrome("kayaka"));
		System.out.println(iv.reverseInt(2345));
	}
}