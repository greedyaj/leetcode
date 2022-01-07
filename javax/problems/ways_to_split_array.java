package javax.problems;

import java.util.List;

public class ways_to_split_array {
    public static void main(String[] args) {
        System.out.println(number_of_ways_to_split_array(List.of(10, 4, -8, 7)));
    }

    static int number_of_ways_to_split_array(List<Integer> arr) {
        int arrayLength  = arr.size();
        int[] presum = new int[arrayLength];
        presum[0] = arr.get(0);
        for (int index = 1; index < arrayLength; index ++) {
            presum[index] = presum[index - 1] + arr.get(index);
        }

        int splitIndex = 0;
        int waysToSplit = 0;
        while (splitIndex < arrayLength - 1) {
            if (presum[splitIndex] > (presum[arrayLength - 1] - presum[splitIndex])) {
                waysToSplit ++;
            }
            splitIndex ++;
        }  
        return waysToSplit;
    }
}