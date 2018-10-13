import java.util.*;

public class FindDuplicateCharacters {
	public static void printDuplicateCharacters(String word) {
		char[] characters = word.toCharArray();

		//building the Hash Map
		Map<Character, Integer> charMap = new HashMap<Character, Integer>();
		for (Character ch: characters) {
			if( charMap.containsKey(ch)) {
				charMap.put(ch, charMap.get(ch)+1);
			} else {
				charMap.put(ch, 1);
			}
		}

		Set<Map.Entry<Character, Integer>> entrySet = charMap.entrySet();
		for (Map.Entry<Character, Integer> entry: entrySet) {
			if (entry.getValue() > 1) {
				System.out.printf("%s : %d %n", entry.getKey(), entry.getValue());
			}
		}

	}

	public static void main(String[] args) {
		printDuplicateCharacters("My name is Kedar Pujara");

	}


}
