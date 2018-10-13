public class IsPalindrome {
	public boolean isPalind(String s) {
		if (s == null) {
			System.out.println("Null val");
			return false;
		}
		if(s.length() == 0 || s.length() == 1) return true;
		if(s.charAt(0) == s.charAt(s.length()-1)) {
			return isPalind(s.substring(1, s.length()-1));
		}
		return false;
	}	

	// public boolean isPalindInt(int st) {
	// 	String s = Integer.toString(st);
	// 	if (s == null) {
	// 		System.out.println("Null val");
	// 		return false;
	// 	}
	// 	if(s.length() == 0 || s.length() == 1) return true;
	// 	if(s.charAt(0) == s.charAt(s.length()-1)) {
	// 		s = s.substring(1, s.length()-1);
	// 		st = Integer.parseInt(s);
	// 		return isPalind(st);
	// 	}
	// 	return false;
	// }	

	public String 
	public static void main(String[] args) {
		IsPalindrome pal = new IsPalindrome();
		boolean isPal = pal.isPalind(null);
		System.out.println(isPal);
	}
}