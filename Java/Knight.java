import java.util.Scanner;

class Knight extends Character {
    private boolean isDefending;
    static Scanner scanner = new Scanner(System.in);

    public Knight(String name, int healthPoints) {
        super(name, healthPoints);
        this.isDefending = false;
    }

    public void takeDamage(int damage) {
        if (isDefending) {
            System.out.println(getName() + " blocked the attack! of " + damage + " damage" );
            System.out.println(' ');
            isDefending = false;
        } else {
            super.takeDamage(damage);
        }
    }

    

    public void changeWeapon() {
        Usar_Arma axe = new Usar_Arma("Axe", 8);
        Usar_Arma knife = new Usar_Arma("Knife", 6);
        Usar_Arma sword = new Usar_Arma("Sword", 9);
        while (true) {
        System.out.println("Troque Sua arma Escolha Axe Knife ou Sword");
        System.out.println(' ');
        String arma = scanner.nextLine();
        if(arma.equalsIgnoreCase("Axe")) {
            this.equipWeapon(axe);
            break;
        } else if (arma.equalsIgnoreCase("Knife")) {
            this.equipWeapon(knife);
            break;
        } else if (arma.equalsIgnoreCase("Sword")) {
            this.equipWeapon(sword);
            break;
        }
        this.setUsar_Arma(Usar_Arma);
        }
}
    

    public void defend() {
        isDefending = true;
        System.out.println(getName() + " is defending and will block the next attack!");
        System.out.println(' ');
    }
}


