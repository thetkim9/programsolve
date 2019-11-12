import java.util.*;
public class Main {
	public static void main (String[] args) {
		Scanner read = new Scanner(System.in);
		int N = read.nextInt();
		int[] lst = new int[N+1];
		for (int i = 1; i<=N; i++) {
		    for (int j = 1; j*j<=i; j++) {
		        if (lst[i]>lst[i-j*j]+1 || lst[i]==0)
		            lst[i] = lst[i-j*j] + 1;
		    }
		}
		System.out.println(lst[N]);
	}
}
