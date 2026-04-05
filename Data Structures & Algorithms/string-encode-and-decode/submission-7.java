class Solution {

    private final String DELIMITER = "#";

    public String encode(List<String> strs) {
        /*
        "neet","code","love","you"
        4#neet4#code4#love3#you
        */
        if(strs == null || strs.size() == 0) return "";
        
        StringBuilder encodedString = new StringBuilder();
        for(String word: strs){
            int length = word.length();
            encodedString.append(length);
            encodedString.append(DELIMITER);
            encodedString.append(word);
        }
        return encodedString.toString();

    }

    public List<String> decode(String encodedString) {
        List<String> res = new ArrayList<>();
        if(encodedString.isEmpty() || encodedString.length() == 0) return res;
        int index = 0;
        int length = encodedString.length();
        
        while(index < length){
            int indexOfDelimiter = encodedString.indexOf(DELIMITER, index);
            int wordLength = Integer.valueOf(encodedString.substring(index, indexOfDelimiter));
            res.add(encodedString.substring(indexOfDelimiter + 1, indexOfDelimiter + 1 + wordLength));
            index = index + 1 + wordLength + 1;
        }
        return res;
    }
}
