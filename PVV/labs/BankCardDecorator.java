public class BankCardDecorator extends ElectronicCardDecorator {
    public BankCardDecorator(IElectronicCard card) {
        super(card);
    }

    @Override
    public String getInfo() {
        return super.getInfo() + " + Банковская карта";
    }
}
