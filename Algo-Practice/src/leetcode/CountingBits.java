package leetcode;

import java.util.Arrays;

public class CountingBits {

	boolean isOne(char c) {
		return c == '1';
	}

	public int[] countBits(int n) {
		int[] ans = new int[n + 1];

		for (int i = 0; i <= n; i++) {
			System.out.print(Integer.toBinaryString(i) + ", ");
			String b = Integer.toBinaryString(i);
			int count = 0;
			for (int j = 0; j < b.length(); j++) {
				if (b.charAt(j) == '1')
					++count;
			}
			ans[i] = count;
		}

		return ans;
	}

	public static void main(String[] args) {
		CountingBits obj = new CountingBits();
		System.out.println("\n" + Arrays.toString(obj.countBits(5)));
	}

}
