def converter_quantidade(texto):
    try:
        return int(texto)
    except ValueError:
        return None


print(converter_quantidade("12"))
print(converter_quantidade("0"))
print(converter_quantidade("doze"))

