public class Solution {
    public uint reverseBits(uint n) {
        string str = Convert.ToString(n, 2);
        char[] charArr = str.ToCharArray();
        int zerosToAdd = 32 - charArr.Length;
        Array.Reverse(charArr);
        string reversed = new string(charArr);

        for (int i = 0; i < zerosToAdd; i++){
            reversed += "0";
        }

        return Convert.ToUInt32(reversed, 2);
    }
}