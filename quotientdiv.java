import java.util.Scanner;
public class quotientdiv {

	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		System.out.println("Please Input dividend: ");
		int dividend = x.nextInt();
		System.out.println("Please Input Divisor: ");
	    int divisor = x.nextInt();

	    int quotient = dividend / divisor;
	    int remainder = dividend % divisor;

	    System.out.println("Quotient = " + quotient);
	    System.out.println("Remainder = " + remainder);
	    x.close();
	}

}
