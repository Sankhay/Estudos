import java.util.Scanner;
import java.util.Random;

public class Main {
    static Random random = new Random();
    static Character Player = null;
    static Character Player2 = null;

    static Usar_Arma axe = new Usar_Arma("Axe", 8);
    static Usar_Arma knife = new Usar_Arma("Knife", 6);
    static Usar_Arma sword = new Usar_Arma("Sword", 9);

    static Usar_Arma orb = new Usar_Arma("Orb", 8);
    static Usar_Arma staff = new Usar_Arma("Staff", 6);
    static Usar_Arma wands = new Usar_Arma("Wands", 9);

    static Usar_Arma claws = new Usar_Arma("claws", 8);
    static Usar_Arma onslaught = new Usar_Arma("onslaught", 6);
    static Usar_Arma breath_of_fire = new Usar_Arma("breath of fire", 9);

    static String mov1 = null;
    static String mov2 = null;


    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Voce não tem a menor chance");
        while (true) {
            System.out.println("Escolha o seu campeão Knight Wizard or WingedDragon");
            String input = scanner.nextLine();
            if (input.equalsIgnoreCase("Knight")) {
                System.out.println("Voce Escolheu Knight!!!");
                System.out.println("Escolha o nome do seu bravo Knight");
                String nome = scanner.nextLine();
                Player = new Knight(nome, 150);
                while (true) {
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
                Player = new Wizard(nome, 100);

                while (true) {
                    System.out.println("Poderoso " + Player.getName() + " Escolha sua arma entre Orb, Staff and Wands");
                    System.out.println(" ");
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
                Player = new WingedDragon(nome, 100);
                while (true) {
                    System.out.println("Poderoso " + Player.getName() + " Escolha sua arma entre Claws, Onslaught and Breath of fire");
                    String weapon = scanner.nextLine();
                    if (weapon.equalsIgnoreCase("Claws")) {
                        Player.equipWeapon(claws);
                        break; 
                    } else if (weapon.equalsIgnoreCase("Onslaught")) {
                        Player.equipWeapon(onslaught);
                        break;
                    } else if (weapon.equalsIgnoreCase("Breath of Fire")) {
                        Player.equipWeapon(breath_of_fire);
                        break;
                    } else {
                        System.out.println("Escolha uma Arma valida seu puto!");
                    }
        } break;
    } else {
        System.out.println("Escolha seu personagem de verdade!");
    } 
        }
    while (true) {
        System.out.println("Escolha seu adversario Knight, Wizard ou WingedDragon");
        String adversario = scanner.nextLine();
        if (adversario.equalsIgnoreCase("Knight")) {
            Player2 = new Knight("Destruidor de mundos", 175);
            int chance = random.nextInt(100);
            if (chance < 34) {
                Player2.equipWeapon(sword);
            } else if (chance < 66) {
                Player2.equipWeapon(knife);
            } else {
                Player2.equipWeapon(axe);
            }
            break;
        } else if (adversario.equalsIgnoreCase("Wizard")) {
            Player2 = new Wizard("Patolino o mago", 150);
            int chance = random.nextInt(100);
            if (chance < 34) {
                Player2.equipWeapon(orb);
            } else if (chance < 66) {
                Player2.equipWeapon(staff);
            } else {
                Player2.equipWeapon(wands);
            }
            break;
        } else if (adversario.equalsIgnoreCase("WingedDragon")) {
            Player2 = new WingedDragon("Smaug", 200);
            int chance = random.nextInt(100);
            if (chance < 34) {
                Player2.equipWeapon(claws);
            } else if (chance < 66) {
                Player2.equipWeapon(onslaught);
            } else {
                Player2.equipWeapon(breath_of_fire);
            }
            break;
        } else {
            System.out.println("Escolhe direito!!! e sabiamente");
            System.out.println(' ');
        }  
    }
    System.out.println("Voce esta contra " + Player2.getName());
    System.out.println(' ');
    while (Player.getHealthPoints() > 0 && Player2.getHealthPoints() > 0) {
    if (Player instanceof Knight) {
        Knight knight = (Knight) Player;
        // Chamadas de métodos específicos de Knight
            System.out.println("Escolha seu proximo movimento Atacar, Defender, Trocar Arma, Correr");
            System.out.println(' ');
            String acao = scanner.nextLine();
            System.out.println(' ');
            if (acao.equalsIgnoreCase("Atacar")) {
                knight.attack(Player2);
            } else if (acao.equalsIgnoreCase("Defender")) {
                knight.defend();
            } else if (acao.equalsIgnoreCase("Trocar Arma")) {
                knight.changeWeapon();
            } else if (acao.equalsIgnoreCase("Correr")) {
                Player.Correr();
            }
             else {
                System.out.println("Não digitou certo perdeu a vez PARABENS!!!");
                System.out.println(' ');
            }

        } else if (Player instanceof Wizard) {
            Wizard wizard = (Wizard) Player;
            System.out.println("Escolha seu proximo movimento Atacar, FireBall, Trocar Arma, Carregar Mana, Correr");
            System.out.println(' ');
            String acao = scanner.nextLine();
            System.out.println(" ");
            if (acao.equalsIgnoreCase("Atacar")) {
                wizard.attack(Player2);
            } else if (acao.equalsIgnoreCase("Fireball")) {
                wizard.FireBall(Player2);
            } else if (acao.equalsIgnoreCase("Trocar Arma")) {
                wizard.changeWeapon();
            } else if (acao.equalsIgnoreCase("Carregar Mana")) {
                wizard.LoadMana();
            } else if (acao.equalsIgnoreCase("Correr")) {
                wizard.Correr();
            }
             else {
                System.out.println("Digitou errado perdeu a vez");
                System.out.println(' ');
            }
        } else if (Player instanceof WingedDragon) {
            WingedDragon dragon = (WingedDragon) Player;
            System.out.println("Escolha seu proximo movimento Atacar, Agilidade ou Voar"); 
            System.out.println(" ");
            String acao = scanner.nextLine();
            System.out.println(" ");
            if (acao.equalsIgnoreCase("Atacar")) {
                dragon.attack(Player2);
            } else if (acao.equalsIgnoreCase("Agilidade")) {
                dragon.agility();
            } else if (acao.equalsIgnoreCase("Voar")) {
                dragon.Voar();
            }
             else {
                System.out.println("Parabens digitou errado perdeu a vez");
            }
        }
     if (Player2 instanceof Knight) {
        Knight knight2 = (Knight) Player2;
        int chance = random.nextInt(100);
        String acao = null;
        if (chance > 50) {
            acao = "Atacar";
        } else {
            acao = "Defender";
        }
        if (acao.equals("Atacar")) {
            knight2.attack(Player);
        } else if (acao.equalsIgnoreCase("Defender")) {
            knight2.defend();
        } 
  } else if (Player2 instanceof Wizard) {
    Wizard wizard2 = (Wizard) Player2;
    String acao = null;
    int chance = random.nextInt(100);
    if (chance > 25) {
        acao = "Atacar";
    } else {
        acao = "Fireball";
    }
    if (acao.equalsIgnoreCase("Atacar")) {
        wizard2.attack(Player);
    } else if (acao.equalsIgnoreCase("Fireball")) {
        wizard2.FireBall(Player);
    }
  } else {
    WingedDragon wingedDragon2 = (WingedDragon) Player2;
    String acao = null;
    int chance = random.nextInt(100);
    if (chance > 25) {
        acao = "Atacar";
    } else {
        acao = "Agility";
    }
    if (acao.equalsIgnoreCase("Atacar")) {
        wingedDragon2.attack(Player);
    } else if (acao.equalsIgnoreCase("Agility")) {
        wingedDragon2.agility();
    }

} 
  }
}
    };

    

    
     
    
    


