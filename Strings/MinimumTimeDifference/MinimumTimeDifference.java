import java.util.*;
class MinimumTimeDifference{
  public int findMinDiff(List<String> timePoints){
    return 0;
  }

  public int stringDiff(String string1, String string2){
    //Try str2-str1
    String[] str1 = string1.split(":");
    String[] str2 = string2.split(":");
    int hour1 = Integer.parseInt(str1[0]);
    int hour2 = Integer.parseInt(str2[0]);
    int minute1 = Integer.parseInt(str1[1]);
    int minute2 = Integer.parseInt(str2[1]);
    int finalHour = 0;
    int finalMin = 0;
    if((hour1 - hour2) > 12){
      finalHour = 24 + hour2 - hour1;
      finalMin = minute2 - minute1;
    } else {
      finalHour = hour1 - hour2;
      finalMin = minute1 - minute2;
    }
    return finalHour*60 + finalMin;
  }

  public static void main(String[] args) {
    MinimumTimeDifference mtd = new MinimumTimeDifference();
    System.out.println(mtd.stringDiff("23:59", "12:50"));
    //System.out.println(mtd.findMinDiff(["23:59","00:00"]));
  }
}
