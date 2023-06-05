class Character {
    private String name;
    public int healthPoints;
    private Usar_Arma Usar_Arma;

    public Character(String name, int healthPoints) {
        this.name = name;
        this.healthPoints = healthPoints;
    }

    public void ChooseName(String nome) {
        this.name = nome;
    }

    public void attack(Character opponent) {
        int damagePoints = Usar_Arma.getDamage();
        opponent.takeDamage(damagePoints);
        System.out.println(this.name + " attacked " + opponent.getName() + " for " + damagePoints + " damage.");
    }

    public String correr() {
        System.out.println("Correu Igual um Covarde");
        return "correu Igual um COVARDE";
    }

    public void takeDamage(int damage) {
        this.healthPoints -= damage;
        System.out.println(this.name + " took " + damage + " damage.");
        System.out.println("Now " + this.name + " have " + this.healthPoints + " of life");
        if (this.healthPoints <= 0) {
            System.out.println(this.name + " has been defeated.");
        }
    }

    public String getName() {
        return this.name;
    }

    public int getHealthPoints() {
        return this.healthPoints;
    }

    public void equipWeapon(Usar_Arma Usar_Arma) {
        this.Usar_Arma = Usar_Arma;
        System.out.println(this.name + " has equipped a " + Usar_Arma.getName() + " .");
    }
}
