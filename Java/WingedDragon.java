import java.util.Random;
import java.util.Scanner;

class WingedDragon extends Character {
    public WingedDragon(String name, int healthPoints) {
        super(name, healthPoints);
    }
    int agility = 0;
    static boolean result = false;

    static Scanner scanner = new Scanner(System.in);
    Random random = new Random();

    public void changeWeapon() {
        Usar_Arma claws = new Usar_Arma("Claws", 8);
        Usar_Arma onslaught = new Usar_Arma("Onslaught", 6);
        Usar_Arma breath_of_fire = new Usar_Arma("Breath of fire", 9);
        while (true) {
        System.out.println("Troque Sua arma Escolha Claws, Onslaught ou Breath of fire");
        String arma = scanner.nextLine();
        if(arma.equalsIgnoreCase("Claws")) {
            this.equipWeapon(claws);
            break;
        } else if (arma.equalsIgnoreCase("Onslaught")) {
            this.equipWeapon(onslaught);
            break;
        } else if (arma.equalsIgnoreCase("Breath of fire")) {
            this.equipWeapon(breath_of_fire);
            break;
        } else {
            System.out.println("Escreveu errado perdeu a vez");
            System.out.println(' ');
            break;
        }
        }
}

    public void Correr() {

    }

    public void Voar() {
        this.healthPoints = 0;
        System.out.println("Voce voa igual um dragao covarde e inutil");
        System.out.println(" ");
    }

    public void agility() {
        System.out.println("O Dragão voa rapido com o poder dos ventos");
        System.out.println(' ');
        agility = 2;
    }

    public void takeDamage(int damage) {
        int chance = random.nextInt(100);
        if (agility == 0) {
            result = chance < 80;
        } else {
            result = chance < 30;
            agility = agility - 1;
        }
        if (result) {
            System.out.println("O Dragão Sofre o Dano de " + damage + "!!!");
            System.out.println(' ');
            super.takeDamage(damage);
        } else {
            System.out.println("É incrivel o Dragão Desvia");
            System.out.println(' ');
        }
        
    }
}

