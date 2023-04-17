string = input ("Informe  a palavra que gostaria de inverter: ").strip()

s = list(string)

i = 0
j = 1

while (i < len (s)):

    s[i] = string[len(string) - j]  

    i = i + 1
    j = j + 1

new_s = "".join(s)

print (f"\nA palavra que gostaria de inverter é: {string}.")
print (f"\nA palavra invertertida é: {new_s}.")
