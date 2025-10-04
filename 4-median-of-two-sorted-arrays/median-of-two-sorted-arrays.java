class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int totalLength = nums1.length + nums2.length;  //toplam eleman sayısı
        int[] numbers = new int[totalLength];   //birleştirilecek dizinin oluşturulması

        System.arraycopy(nums1 , 0 , numbers , 0 , nums1.length);
        System.arraycopy(nums2 , 0 , numbers , nums1.length , nums2.length);

        Arrays.sort(numbers);   //Sayıların sıralaması.

        if(totalLength%2==1){
            return (double)numbers[(totalLength-1)/2];
        }
        else{
            double median = (numbers[totalLength/2] + numbers[(totalLength/2)-1])/2.0;
            return median;
        }

    }
}