import java.util.Scanner;

public class Main {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        while (true) {
            System.out.println("Escolha o seu campeão Knight Wizard or WingedDragon");
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("Knight")) {
                System.out.println("Voce Escolheu Knight!!!");
                System.out.println("Escolha o nome do seu bravo Knight");
                String nome = scanner.nextLine();
                Knight Player = new Knight(nome, 150);
                while (true) {
                    Usar_Arma axe = new Usar_Arma("Axe", 8);
                    Usar_Arma knife = new Usar_Arma("Knife", 6);
                    Usar_Arma sword = new Usar_Arma("Sword", 9);
                    System.out.println("Poderoso " + Player.getName() + " Escolha sua arma entre Axe, Knife and Sword");
                    String weapon = scanner.nextLine();
                    if (weapon.equalsIgnoreCase("Axe")) {
                        Player.equipWeapon(axe);
                        break;
                    } else if (weapon.equalsIgnoreCase("Knife")) {
                        Player.equipWeapon(knife);
                        break;
                    } else if (weapon.equalsIgnoreCase("Sword")) {
                        Player.equipWeapon(sword);
                        break;
                    } else {
                        System.out.println("Escolha uma Arma valida seu puto!");
                    }
                } break;
            } 
            
            
            
            
            
            else if (input.equalsIgnoreCase("Wizard")) {
                System.out.println("Voce Escolheu Wizard!!!");
                System.out.println("Escolha o nome do seu sabio WIZARD!");
                String nome = scanner.nextLine();
                Wizard Player = new Wizard(nome, 100);

                while (true) {
                    Usar_Arma orb = new Usar_Arma("Orb", 8);
                    Usar_Arma staff = new Usar_Arma("Staff", 6);
                    Usar_Arma wands = new Usar_Arma("Wands", 9);
                    System.out.println("Poderoso " + Player.getName() + " Escolha sua arma entre Orb, Staff and Wands");
                    String weapon = scanner.nextLine();
                    if (weapon.equalsIgnoreCase("Orb")) {
                        Player.equipWeapon(orb);
                        break; 
                    } else if (weapon.equalsIgnoreCase("Staff")) {
                        Player.equipWeapon(staff);
                        break;
                    } else if (weapon.equalsIgnoreCase("Wands")) {
                        Player.equipWeapon(wands);
                        break;
                    } else {
                        System.out.println("Escolha uma Arma valida seu puto!");
                    }
                } break;
            }
            
            
            
            else if (input.equalsIgnoreCase("WingedDragon")) {
                System.out.println("Voce Escolheu UM FUDENDO DRAGÂO");
                System.out.println("Escolha o nome do seu PODEROSO DRAGÂO");
                String nome = scanner.nextLine();
                WingedDragon Player = new WingedDragon(nome, 100);
                while (true) {
                    Usar_Arma orb = new Usar_Arma("Orb", 8);
                    Usar_Arma staff = new Usar_Arma("Staff", 6);
                    Usar_Arma wands = new Usar_Arma("Wands", 9);
                    System.out.println("Poderoso " + Player.getName() + " Escolha sua arma entre Axe, Knife and Sword");
                    String weapon = scanner.nextLine();
                    if (weapon.equalsIgnoreCase("Orb")) {
                        Player.equipWeapon(orb);
                        break; 
                    } else if (weapon.equalsIgnoreCase("Staff")) {
                        Player.equipWeapon(staff);
                        break;
                    } else if (weapon.equalsIgnoreCase("Wands")) {
                        Player.equipWeapon(wands);
                        break;
                    } else {
                        System.out.println("Escolha uma Arma valida seu puto!");
                    }
        } break;
    } else {
        System.out.println("Escolha seu personagem de verdade!");
    } 
        }}};

    
     
    
    


