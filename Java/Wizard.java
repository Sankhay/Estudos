import java.util.Scanner;

class Wizard extends Character {
    private int Mana;
    static Scanner scanner = new Scanner(System.in);

    public Wizard(String name, int healthPoints) {
        super(name, healthPoints);
        Mana = 100;
    }

    public void LoadMana() {
        System.out.println("O mago carrega o seu infinito poder");
        System.out.println(" ");
        Mana = Mana + 30;
    }

    public void FireBall(Character oponnent) {
        if (Mana == 0) {
            System.out.println("Devia ter contado sua mana ta sem perdeu o round PARABENS!!!");
            System.out.println(' ');
        } else {
            oponnent.takeDamage(17);
            this.Mana = Mana - 10;
            System.out.println(oponnent.getName() + "Tomou 17 de dano!");
            System.out.println(' ');
        }
        
    }

    public void changeWeapon() {
        Usar_Arma orb = new Usar_Arma("Orb", 8);
        Usar_Arma staff = new Usar_Arma("Staff", 6);
        Usar_Arma wands = new Usar_Arma("Wands", 9);
        while (true) {
        System.out.println("Troque Sua arma Escolha Orb, Staff ou Wands");
        String arma = scanner.nextLine();
        System.out.println(' ');
        if(arma.equalsIgnoreCase("Claws")) {
            this.equipWeapon(orb);
            break;
        } else if (arma.equalsIgnoreCase("Staff")) {
            this.equipWeapon(staff);
            break;
        } else if (arma.equalsIgnoreCase("Wands")) {
            this.equipWeapon(wands);
            break;
        } else {
            System.out.println("Escreveu errado perdeu a vez");
            System.out.println(' ');
            break;
        }
        }
}
}