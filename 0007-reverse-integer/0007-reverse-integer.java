class Solution {
    public int reverse(int x) {
        int count;
        int rem=0;
        if(x==0)
        return 0;
        if(x==1)
        return 1;
        while(x!=0)
        {
         count=x%10;
         if (rem > Integer.MAX_VALUE / 10 || rem < Integer.MIN_VALUE / 10) {
    return 0;
}
         rem=rem*10+count;
         x=x/10;   
        }
       return rem;
    }
}