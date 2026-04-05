class Solution {
    public int longestConsecutive(int[] nums) {

        Set<Integer> set = new HashSet<>();
        Arrays.stream(nums).forEach(x -> set.add(x));
        int maxLength = 0;
        for(int i=0; i<nums.length; i++){

            if(set.contains(nums[i]-1)){
                continue;
            }else{
                int length = 1;
                int num = nums[i];
                while(set.contains(num+1)){
                    length++;
                    ++num;
                }
                maxLength = Math.max(maxLength, length);
            }
        }
        return maxLength;

           
    }
}
