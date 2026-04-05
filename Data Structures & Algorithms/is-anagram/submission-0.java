class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!=t.length()){
            return false;
        }

        Map<Character, Integer> key = new HashMap<>();

        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            key.put(ch, key.getOrDefault(ch,0)+1);
        }

        for(int i=0; i<t.length(); i++) {
            char ch = t.charAt(i);
            if(!key.containsKey(ch)) return false;

            int val = key.get(ch);
            if(val == 1){
                key.remove(ch);
            }else{
                key.put(ch, val-1);
            }
        }

        //if(!key.isEmpty()) return false;

        return true;
    }
}
