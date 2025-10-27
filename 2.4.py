import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()
values = []
for child in root.findall('.//Valute'):
    value_text = child.find("Value").text
    value_num = float(value_text.replace(',', '.'))
    values.append(value_num)
if values:
    average = sum(values) / len(values)
    print(f": {average:.4f}")
    print(f" {len(values)} ")
    print(f"min: {min(values):.4f}")
    print(f"max: {max(values):.4f}")
