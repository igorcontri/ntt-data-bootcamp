def car_register(brand, model, year, lic_plate):
    print(f"Car registered successfully! {brand} - {model} - {year} - {lic_plate}")

car_register(**{"brand": "Fiat", "model": "Palio", "year": 1999, "lic_plate": "ABC-1234"})

# Parecido com os argumentos nomeados
# Estou simplesmente passando um dicionário com chave e valor para os respectivos argumentos

# As chaves, assim como nos "argumentos nomeados", precisam ter os mesmos nomes dos parâmetros da função