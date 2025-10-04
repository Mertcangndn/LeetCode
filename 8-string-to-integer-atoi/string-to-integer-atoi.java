class Solution {
    public int myAtoi(String s) {
        s = s.trim();   //Baştaki ve sonraki boşluklardan kurtulundu

        if(s.length()==0){
            return 0;
        }

        int sign = 1; // sonda çarpılacak, default 1;
        int index = 0;
        long result = 0;
        
        if(s.charAt(index) == '-'){
            index++;
            sign = -1;
        }
        else if(s.charAt(index) == '+'){
            index++;
        }
        else if(!Character.isDigit(s.charAt(index))){
            return 0;
        }

        for(; index<s.length() ; index++){
            char c = s.charAt(index);

            if(!Character.isDigit(c)){
                break;
            }

            int digit = c - '0';
            result = result*10 + digit;

            if(sign == 1 && result>=Integer.MAX_VALUE){
                return Integer.MAX_VALUE;
            }
            if(sign == -1 && result*sign<=Integer.MIN_VALUE){
                return Integer.MIN_VALUE;
            }
        }
        return (int) (sign*result);
    }
}