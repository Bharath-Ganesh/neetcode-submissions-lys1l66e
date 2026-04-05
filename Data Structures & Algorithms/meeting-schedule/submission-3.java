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
    public boolean canAttendMeetings(List<Interval> intervals) {

        int n = intervals.size();
        if(n == 0 || n == 1){
            return true;
        }

        Collections.sort(intervals, (a, b) -> a.start - b.start);
        int start = intervals.get(0).start;
        int end = intervals.get(0).end;
        for(int index = 1; index < n; index++){
            if(intervals.get(index).start < end){
                return false;
            }else {
                start = intervals.get(index).start;
                end = intervals.get(index).end;               
            }
        }
        return true;
    }
}
