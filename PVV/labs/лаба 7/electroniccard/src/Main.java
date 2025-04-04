public class Main {
    public static void main(String[] args) {
        // Создание базовой карты
        IElectronicCard basicCard = new BasicElectronicCard();

        // Добавление функций одной за другой
        IElectronicCard passportCard = new PassportDecorator(basicCard);
        IElectronicCard insuranceCard = new InsurancePolicyDecorator(passportCard);
        IElectronicCard bankCard = new BankCardDecorator(insuranceCard);

        // Вывод информации
        System.out.println(bankCard.getInfo());
    }
}
