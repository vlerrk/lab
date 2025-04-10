public class PassportDecorator extends ElectronicCardDecorator {
    public PassportDecorator(IElectronicCard card) {
        super(card);
    }

    @Override
    public String getInfo() {
        return super.getInfo() + " + Паспорт";
    }
}
