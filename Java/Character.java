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
        System.out.println(this.name + " Atacou " + opponent.getName() + " em " + damagePoints + " de dano.");
        System.out.println(" ");
        opponent.takeDamage(damagePoints);
        return name;
    }

    public void Correr() {
        this.healthPoints = 0;
        System.out.println("Voce corre igual um covarde");
        System.out.println(" ");
    }

    public void takeDamage(int damage) {
        this.healthPoints -= damage;
        System.out.println("Agora " + this.name + " tem " + this.healthPoints + " de vida");
        System.out.println(' ');
        if (this.healthPoints <= 0) {
            System.out.println(this.name + " Foi derrotado.");
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
        System.out.println(this.name + " equipou uma " + Usar_Arma.getName() + " .");
        System.out.println(' ');
    }
}
