class Solution {

    private static final Character CONST = '#';

    public String encode(List<String> strs) {

        StringBuilder encodeString = new StringBuilder();
        for(String word : strs){
            int len = word.length();
            encodeString.append(len);
            encodeString.append(CONST);
            encodeString.append(word);
        }
        return encodeString.toString();
    }

    public List<String> decode(String str) {

        List<String> results = new ArrayList<>();
        int index = 0;
        int n =  str.length();
        while(index < n) {
            String digits = findIndex(str, index);
            index += digits.length() + 1;
            int length = Integer.parseInt(digits);
            String word = str.substring(index, index + length);
            results.add(word);
            index += length;
        }
        return results;
    }

    private String findIndex(String word, int low){
        String index = "";
        for(int i = low; i < word.length(); i++){
            Character ch = word.charAt(i);
            if(ch == CONST) break;
            index += ch;
        }
        return index;
    }
}
