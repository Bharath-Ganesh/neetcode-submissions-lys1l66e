class Solution {

   Character DELIMITER = '#';
    public String encode(List<String> strs) {

        StringBuilder encodedString = new StringBuilder();
        for(String word:  strs){
            int len = word.length();
            encodedString.append(len);
            encodedString.append(DELIMITER);
            encodedString.append(word);
        }
        return encodedString.toString();
    }

    public List<String> decode(String str) {

        List<String> result = new ArrayList<>();
        int len = 0;
        while(len < str.length()) {
            int index = str.indexOf(DELIMITER,len);
            int length;
            if(index != -1){
                length = Integer.parseInt(str.substring(len, index));
                len+=2;
                String word = str.substring(len, len + length);
                len+=length;
                result.add(word);
            }else {
                result.add(str.substring(len));
                break;
            }
        }
        return result;
    }
}
