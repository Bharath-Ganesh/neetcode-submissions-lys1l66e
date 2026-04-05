class Solution {


    Character DELIMITER = '#';

    public String encode(List<String> strs) {
        StringBuilder encodedStr = new StringBuilder();
        for (String word : strs) {
            encodedStr.append(word.length()).append(DELIMITER).append(word);
        }
        return encodedStr.toString();
    }

    public List<String> decode(String str) {

        List<String> decodedList = new ArrayList<>();
        int index = 0;

        while (index < str.length()) {
            // Extract the length of the next word
            int delimiterPos = str.indexOf(DELIMITER, index);
            int length = Integer.parseInt(str.substring(index, delimiterPos));
            index = delimiterPos + 1;  // Move past the delimiter

            // Extract the word
            String word = str.substring(index, index + length);
            decodedList.add(word);
            index += length;  // Move to the next encoded word
        }

        return decodedList;
    }
}
