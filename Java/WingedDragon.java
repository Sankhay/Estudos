import java.util.Random;

class WingedDragon extends Character {
    public WingedDragon(String name, int healthPoints) {
        super(name, healthPoints);
    }

    Random random = new Random();



    public void takeDamage(int damage) {
        int chance = random.nextInt(100);
        boolean result = chance < 80;

        if (result) {
            System.out.println("O Dragão Sofre o Dano de " + damage + "!!!");
            this.healthPoints -= damage;
        } else {
            System.out.println("É incrivel o Dragão Desvia");
        }
    }
}
