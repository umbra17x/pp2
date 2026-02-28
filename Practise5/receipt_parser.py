import re
import json

# Деньги в формате: "308,00" или "7 330,00"
MONEY_RE = r"\d{1,3}(?: \d{3})*,\d{2}"

def normalize_money(m: str) -> float:
    # "7 330,00" -> 7330.00
    return float(m.replace(" ", "").replace(",", "."))

def main():
    with open("raw.txt", "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    lines = text.splitlines()

    # 1) Все цены (все денежные суммы в чеке)
    prices_raw = re.findall(MONEY_RE, text)
    prices = [normalize_money(p) for p in prices_raw]

    # 2) Названия товаров: строка сразу после "1.", "2.", ...
    products = []
    for i in range(len(lines) - 1):
        if re.fullmatch(r"\s*\d+\.\s*", lines[i]):   # строка вида "12."
            name = lines[i + 1].strip()
            if name:
                products.append(name)

    # 3) Total amount: берем из "ИТОГО:"
    total = None
    m_total = re.search(r"ИТОГО:\s*\n\s*(" + MONEY_RE + r")", text)
    if m_total:
        total = normalize_money(m_total.group(1))
    else:
        # запасной вариант: если вдруг "ИТОГО:" в одной строке
        m_total2 = re.search(r"ИТОГО:\s*(" + MONEY_RE + r")", text)
        if m_total2:
            total = normalize_money(m_total2.group(1))

    # 4) Дата и время (обычно "Время: 18.04.2019 11:13:58")
    date = time = None
    m_dt = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})", text)
    if m_dt:
        date, time = m_dt.group(1), m_dt.group(2)
    else:
        # запасной вариант: отдельно дата и отдельно время
        m_date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)
        m_time = re.search(r"\d{2}:\d{2}:\d{2}", text)
        date = m_date.group(0) if m_date else None
        time = m_time.group(0) if m_time else None

    # 5) Способ оплаты
    payment_method = None
    if re.search(r"Банковская\s*карта", text, re.IGNORECASE):
        payment_method = "Банковская карта"
    elif re.search(r"Наличные", text, re.IGNORECASE):
        payment_method = "Наличные"
    elif re.search(r"\bVisa\b|\bMastercard\b", text, re.IGNORECASE):
        payment_method = "Card"

    # 6) JSON структура
    result = {
        "products": products,
        "prices": prices,              # все суммы, найденные в чеке
        "total": total,                # итог по чеку
        "date": date,
        "time": time,
        "payment_method": payment_method,
        "meta": {
            "products_count": len(products),
            "prices_count": len(prices),
        }
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()