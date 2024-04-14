public class Test {
    public static void main(String[] args) {
        int[] arr = new int[]{1,2,3,4,5};
        int[] arr2 = arr;
        arr2[0] = 0;
        for (int i: arr){
            System.out.println(i);
        }

        int x = 10;
        int y = x;
        y = 20;
        System.out.println(y);
    }
}
