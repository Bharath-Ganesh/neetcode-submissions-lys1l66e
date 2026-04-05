class Solution {
        public List<List<String>> groupAnagrams(String[] strs) {
        
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        for(String word: strs){
            char[] arr1 = word.toCharArray();
            Arrays.sort(arr1);
            String alphabeticalWord = new String(arr1);
            List<String> wordGroup;
            if(map.containsKey(alphabeticalWord)){
                wordGroup = map.get(alphabeticalWord);
                wordGroup.add(word);
            }else{
                wordGroup = new ArrayList<>();
                wordGroup.add(word);      
            }
            map.put(alphabeticalWord, wordGroup);
        }

        for(Map.Entry<String, List<String>> keyMap : map.entrySet()) {
            result.add(keyMap.getValue());
        }
        return result;
    }
}
