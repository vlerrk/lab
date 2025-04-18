from lxml import etree # type: ignore

def validate_xml(xml_path, xsd_path):
    try:
        xml_doc = etree.parse(xml_path)
        xsd_doc = etree.parse(xsd_path)
        xmlschema = etree.XMLSchema(xsd_doc)
        if xmlschema.validate(xml_doc):
            print("XML валиден!")
        else:
            print("Ошибки валидации:")
            print(xmlschema.error_log)
    except Exception as e:
        print(f"Ошибка: {e}")

validate_xml("library.xml", "library.xsd")