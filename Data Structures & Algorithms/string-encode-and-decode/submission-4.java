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
            int length = findIndex(str, index);
            index += 2;
            String word = str.substring(index, index + length);
            results.add(word);
            index += length;
        }
        return results;
    }

    private int findIndex(String word, int low){
        int index = 0;
        for(int i = low; i < word.length(); i++){
            Character ch = word.charAt(i);
            if(ch == CONST) break;
            index = index * 10 + (ch - '0');
        }
        return index;
    }
}
