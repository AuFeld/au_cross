closing_price_sum = 0

with open('data/APD.csv') as f:
    content = f.readlines()[-50:]
    for line in content:
        print(line)
        tokens = line.split(",")
        close = tokens(4)

        closing_price_sum += float(close)

print(closing_price_sum / 50)