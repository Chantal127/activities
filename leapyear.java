import java.util.Scanner;
public class leapyear {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner x = new Scanner(System.in);
		System.out.println("Please enter a year:");
		int year = x.nextInt();
		 boolean leap = false;

	        if(year % 4 == 0)
	        
	        {
	            if( year % 100 == 0)
	            {
	                if ( year % 400 == 0)
	                    leap = true;
	                else
	                    leap = false;
	            }
	            else
	                leap = true;
	        }
	        else
	        	leap = false;

	        if(leap==true)
	            System.out.println(year + " is a Leap Year.");
	        else
	            System.out.println(year + " is not  Leap Year.");
	        x.close();
	}

}
