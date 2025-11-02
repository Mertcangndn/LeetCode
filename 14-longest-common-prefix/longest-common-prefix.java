class Solution {
    public String longestCommonPrefix(String[] strs) {

        String temp = strs[0];
        int lastIndex = temp.length();
        
        for(int i=1 ; i<strs.length ; i++){
            while(lastIndex>=0){
                temp = temp.substring(0,lastIndex);
                if(strs[i].indexOf(temp)==0){
                    break;
                }else{
                    lastIndex--;
                }
            }
        }

        return temp;
    }
}