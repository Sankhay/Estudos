class Knight extends Character {
    private boolean isDefending;

    public Knight(String name, int healthPoints) {
        super(name, healthPoints);
        this.isDefending = false;
    }

    public void takeDamage(int damage) {
        if (isDefending) {
            System.out.println(getName() + " blocked the attack! of " + damage + " damage" );
            System.out.println(getHealthPoints());
            isDefending = false;
        } else {
            super.takeDamage(damage);
        }
    }

    public void defend() {
        isDefending = true;
        System.out.println(getName() + " is defending and will block the next attack!");
    }
}


