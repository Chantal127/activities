import java.util.Scanner;
public class CalcSwitchcase {


	public static void main(String[] args) {
		Scanner x = new Scanner(System.in);
		System.out.println("Input First Number: ");
		int first = x.nextInt();
		System.out.println("Input Second Number: ");
		int second = x.nextInt();
				
				System.out.println("You can perform operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division");
				System.out.println("Select operation from 1,2,3,4 : ");
				int operator = x.nextInt();
				
				switch (operator){
				    case 1:
				        int add = first + second;
				        System.out.println("The answer in " + first +" + " +second + " is " + add);
				        break;
				    case 2:
				        int sub = first - second;
				        System.out.println("The answer in " + first +" - " +second + " is " + sub);
				        break;
				    case 3:
				        int mul = first * second;
				        System.out.println("The answer in " + first +" * " +second + " is " + mul);
				        break;
				    case 4:
				        int div = first / second;
				        System.out.println("The answer in " + first +" / " +second + " is " + div);
				        break;
				    default:
				        System.out.println("Invalid operator!");
				        break;
				}
				x.close();
		
	}

}