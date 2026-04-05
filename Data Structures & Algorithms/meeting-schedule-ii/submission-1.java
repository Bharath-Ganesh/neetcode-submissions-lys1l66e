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

        int n = intervals.size();
        int[] startMeeting = new int[n];
        int[] endMeeting = new int[n];
        int index = 0;
        for(Interval interval : intervals){
            startMeeting[index] = interval.start;
            endMeeting[index] = interval.end;
            index += 1;
        }

        Arrays.sort(startMeeting);
        Arrays.sort(endMeeting);

        int pt1 = 0;
        int pt2 = 0;
        int minMeetingRoom = 0;
        int room = 0;
        while(pt1 < n && pt2 < n){

            if(startMeeting[pt1] < endMeeting[pt2]){
                pt1 += 1;
                room += 1;
            }else {
                pt2 += 1;
                room -=1;
            }
            minMeetingRoom = Math.max(minMeetingRoom, room);
        }
        return minMeetingRoom;
    }
}
