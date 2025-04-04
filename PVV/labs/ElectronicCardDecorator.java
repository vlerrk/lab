public abstract class ElectronicCardDecorator implements IElectronicCard {
    protected IElectronicCard card;

    public ElectronicCardDecorator(IElectronicCard card) {
        this.card = card;
    }

    @Override
    public String getInfo() {
        return card.getInfo();
    }
}
