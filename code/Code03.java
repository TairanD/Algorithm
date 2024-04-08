package code;

public class Code03 {
    private static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void heapInsert(int[] arr, int index){
        while (arr[index] > arr[(index-1)>>1] && index > 0){
            swap(arr, index, (index-1)>>1);
            index = (index-1)>>1;
        }
    }
}
