def car_register(brand, model, year, lic_plate):
    print(f"Car registered successfully! {brand} - {model} - {year} - {lic_plate}")

car_register("Fiat", "Palio", 1999, "ACB-2134")

# Metodo tradicional, porem suscetível a erros
# Por exemplo, eu poderia passar ano no campo da marca e a função aceitaria 

# car_register(1999, "Palio", "Fiat", "ACB-2134")

# Dessa forma o programa não apresentaria erros, mas estaria atribuindo valor para a variável errada