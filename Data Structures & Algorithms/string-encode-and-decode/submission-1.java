class Solution {


    Character delimiter = '#';
    public String encode(List<String> strs) {

        StringBuilder result  = new StringBuilder();

        for(int i=0; i<strs.size(); i++){
            String word = strs.get(i);
            int length = word.length();
            result.append(length);
            result.append(delimiter);
            result.append(word);
        }
        return result.toString();
    }

    public List<String> decode(String str) {

        List<String> resultantList = new ArrayList<>();

        int index = 0;
        int n = str.length();

        while(!str.isEmpty() && index<n){
            StringBuilder num = new StringBuilder();
            while(index < n){
                if(str.charAt(index) =='#') break;

                num.append(str.charAt(index));
                index ++;
            }
            int length = Integer.parseInt(num.toString());
            int count = 0;
            index ++;
            StringBuilder word = new StringBuilder();
            while(index<n && count < length){
                word.append(str.charAt(index));
                index++; count++;
            }
            resultantList.add(word.toString());
        }

        return resultantList;
    }
}
