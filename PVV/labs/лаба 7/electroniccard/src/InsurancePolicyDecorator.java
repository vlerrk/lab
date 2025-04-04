public class InsurancePolicyDecorator extends ElectronicCardDecorator {
    public InsurancePolicyDecorator(IElectronicCard card) {
        super(card);
    }

    @Override
    public String getInfo() {
        return super.getInfo() + " + Страховой полис";
    }
}
