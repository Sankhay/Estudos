class Character {
    public String name;
    public int healthPoints;
    public Usar_Arma Usar_Arma;

    public Character(String name, int healthPoints) {
        this.name = name;
        this.healthPoints = healthPoints;
    }

    public Usar_Arma getUsar_Arma() {
        return Usar_Arma;
    }

    public void setUsar_Arma(Usar_Arma usar_Arma) {
        this.Usar_Arma = usar_Arma;
    }

    public void ChooseName(String nome) {
        this.name = nome;
    }

    public String attack(Character opponent) {
        int damagePoints = getUsar_Arma().getDamage();
        System.out.println(this.name + " attacked " + opponent.getName() + " for " + damagePoints + " damage.");
        opponent.takeDamage(damagePoints);
        return name;
    }

    public String correr() {
        System.out.println("Correu Igual um Covarde");
        return "covarde";
        }

    public void takeDamage(int damage) {
        this.healthPoints -= damage;
        System.out.println("Now " + this.name + " have " + this.healthPoints + " of life");
        System.out.println(' ');
        if (this.healthPoints <= 0) {
            System.out.println(this.name + " has been defeated.");
            System.out.println(' ');
        }
    }

    public String getName() {
        return this.name;
    }

    public int getHealthPoints() {
        return this.healthPoints;
    }

    public void equipWeapon(Usar_Arma Usar_Arma) {
        this.setUsar_Arma(Usar_Arma);
        System.out.println(this.name + " has equipped a " + Usar_Arma.getName() + " .");
        System.out.println(' ');
    }
}
