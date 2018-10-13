public class ReverseRecurse {

	public static String reverseRecursively(String str) {
		if (str.length() < 2) {
			return str;
		}
		return reverseRecursively(str.substring(1) + str.charAt(0));
	}


	public static String reverse(String str) {
		StringBuilder input1 = str.
	}

	public static void main(String[] args) {
		reverseRecursively("Kedar");
	}
}