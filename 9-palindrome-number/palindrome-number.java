class Solution {
    public boolean isPalindrome(int x) {

        if (x < 0) {
            return false; // negatif sayılar palindrome olmaz
        }

        StringBuilder xString = new StringBuilder(String.valueOf(x));
        String ters = new StringBuilder(xString).reverse().toString();

        return xString.toString().equals(ters);
    }
}
