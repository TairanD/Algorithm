package grind75q.array;

import java.util.HashMap;
import java.util.Map;

public class TwoSumSolution {
    public int[] bruce(int[] nums, int target) {
        for (int i = 0; i < nums.length-1; i++){
            for (int j = i+1; j < nums.length; j++){
                int sum = nums[i]+nums[j];
                if (sum == target){
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    public static int[] hashSolution(int[] nums, int target){
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (map.containsKey(complement)){
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
