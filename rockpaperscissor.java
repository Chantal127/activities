
import java.util.Scanner;

public class rockpaperscissor {

	public static void main(String[] args) {
		String player;
		String[] list = {"Rock", "Paper", "Scissors"};
		
		Scanner  x= new Scanner(System.in);
		
		int random = (int)Math.floor(Math.random() * 3);
		int playerscore=0, compscore = 0;
		while (true){
			System.out.println("Please Choose: Rock, Paper,Scissors");
			player = x.nextLine();
			String comp = list[random];
			String result = "";
			
			if (player.equals(comp)) {
				result = "Tie!";
			} else if (player.equals("Rock")) {
				if (comp.equals("Scissors")) {
					result = "You Won! " + player + " smashes " + comp+ ".";
					playerscore =+ 1;
				} else {
					result = "You Lose!" + comp + " covers " + player+ ".";
					compscore =+1 ;
					}
				} else if (player.equals("Paper")) {
					if (comp.equals("Rock")) {
						result = "You Won! " + player + " covers " + comp + ".";
						playerscore =+ 1;
					} else {
						result = "You Lose! " + comp + " cuts " + player+ ".";
						compscore =+1 ;
					}
			} else if (player.equals("Scissors")) {
				if (comp.equals("Paper")) {
					result = "You Won! " + player + " cuts " + comp+ ".";
					playerscore =+ 1;
				} else {
					result = "You Lose! " + comp + " smashes " + player+ ".";
					compscore =+1 ;
		}
			} else {
				System.out.println("Invalid! Please check your spelling!");
				continue;
			}
				System.out.println(result);
				System.out.println(" You choose: " + player + "\n Computer choose: " + comp);
				System.out.println(" Player Score: " + playerscore + "\nComputer Score: "+ compscore);
				System.out.println ("Do you want to try again? \n Yes or No");
				String quit = x.nextLine();
				 random = (int)Math.floor(Math.random() * 3);
				if (quit.equals("Yes")) {
					continue;
				}
					else if (quit.equals("No")) {
						System.out.println("Thank you!");
						break;
				}
					else {
						break;
					}
    }
		x.close();
		}
	
	}
