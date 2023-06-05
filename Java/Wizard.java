class Wizard extends Character {
    private int Mana;

    public Wizard(String name, int healthPoints) {
        super(name, healthPoints);
        Mana = 100;
    }

    public void FireBall(Character oponnent) {
        if (Mana == 0) {
            System.out.println("Devia ter contado sua mana ta sem perdeu o round PARABENS!!!");
        } else {
            oponnent.takeDamage(10);
            this.Mana = Mana - 10;
            System.out.println(oponnent.getName() + "Tomou 10 de dano!");
        }
        
    }
}