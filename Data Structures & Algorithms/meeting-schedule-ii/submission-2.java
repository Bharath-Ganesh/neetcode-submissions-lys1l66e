/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        /*
            intervals = [(0,40),(5,10),(15,20)]
            0  5  15
            10 20 40

        */
        int size = intervals.size();
        int[] start = new int[size];
        int[] end = new int[size];
        for(int index = 0; index < size; index++){
            start[index] = intervals.get(index).start;
            end[index] = intervals.get(index).end;
        }
        Arrays.sort(start);
        Arrays.sort(end);

        int minRoomsRequired = 0;
        int maxRoomsAtAnyPoints = 0;

        int sIndex = 0;
        int eIndex = 0;
        while(sIndex < size && eIndex < size){
            
            if(start[sIndex] < end[eIndex]){
                minRoomsRequired += 1;
                sIndex += 1;
            }else {
                minRoomsRequired -= 1;
                eIndex += 1;
            }
            maxRoomsAtAnyPoints = Math.max(maxRoomsAtAnyPoints, minRoomsRequired);
        }
        return maxRoomsAtAnyPoints;


















    }
}
