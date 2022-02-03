def FindPercentage(strAmount):
    # Replace the , with empty.
    a = strAmount.replace(",", "")
    fa = float(a)
    return fa * 0.2

x = "12,34,34,456.90"
print(FindPercentage(x))