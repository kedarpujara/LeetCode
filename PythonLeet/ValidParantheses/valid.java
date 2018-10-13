class Solution {

    public boolean isValid(String s) {
        if(s.length() == 0){
            return true;
        }
        //parantheses = {"}": "{", "]": "[", ")": "("
        HashMap<Character, Character> paran = new HashMap<Character, Character>();
        paran.put('{', '}');
        paran.put('[',']' );
        paran.put('(', ')');

        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < s.length(); i++){
            Character curr = s.charAt(i);
            if(isOpen(curr)){
                stack.push(paran.get(curr));
            }
            else if(isClosed(curr)){
                if (stack.isEmpty()){
                    return false;
                }
                else {
                    Character top = stack.pop();
                    if (curr != top){
                        return false;
                    }
                }
            }
            //System.out.println(stack.peek());
        }
        if (stack.isEmpty()){
            return true;
        }
        return false;
    }

    public boolean isOpen(Character c){
        char[] cAr = new char[] {'{', '(', '['};
        for(char ch : cAr) {
            if (ch == c){
                return true;
            }
        }
        return false;
    }
    public boolean isClosed(Character c){
        char[] cAr = new char[] {'}', ')', ']'};
        for(char ch : cAr) {
            if (ch == c){
                return true;
            }
        }
        return false;
    }


}
