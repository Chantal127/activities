import java.util.Scanner;
public class Fibonacciii {

	public static void main(String[] args) {
		
		int n1=0,n2=1,n3,i;
		Scanner x = new Scanner(System.in);
		int count= x.nextInt();
		 System.out.print(n1+" "+n2);   
		    
	 	 for(i=2;i<count;++i)    
		 {    
		  n3=n1+n2;    
		  System.out.print(" "+n3);    
		  n1=n2;    
		  n2=n3;  
		  x.close();
		 }    
	}

}