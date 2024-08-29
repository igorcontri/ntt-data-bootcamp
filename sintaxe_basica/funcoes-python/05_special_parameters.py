# / faz com que os parametros anteriores a esse operador sejam obrigatoriamente posicionais
# * faz com que os parametros após esse operador sejam obrigatoriamente nomeados


# POSITIONAL ONLY --------------------------------------------------------------------------------------------------------------
print("--- POSITIONAL ONLY ---")
def car_register(model, year, lic_plate, /, brand, engine, fuel ):
    print(model, year, lic_plate, brand, engine, fuel)

car_register("Palio", 1999, "ACB-2134", "Fiat","1.0", fuel="Gas") #VALID
# car_register(model="Palio", year=1999, lic_plate="ACB-2134", brand="Fiat", engine="1.0", fuel="Gas") #INVALID


# KEYWORD ONLY -----------------------------------------------------------------------------------------------------------------
print("--- KEYWORD ONLY ---")
def car_register(*, model, year, lic_plate, brand, engine, fuel):
    print(model, year, lic_plate, brand, engine, fuel)

car_register(model="Palio", year=1999, lic_plate="ACB-2134", brand="Fiat", engine="1.0", fuel="Gas") #VALID
# car_register("Palio", 1999, "ACB-2134", brand="Fiat", engine="1.0", fuel="Gas") #INVALID


# HIBRID -----------------------------------------------------------------------------------------------------------------------
print("--- HIBRID---")
def car_register(model, year, lic_plate, /, *, brand, engine, fuel ):
    print(model, year, lic_plate, brand, engine, fuel)

car_register("Palio", 1999, "ACB-2134", brand="Fiat", engine="1.0", fuel="Gas") #VALID
# car_register(model="Palio", year=1999, lic_plate="ACB-2134", brand="Fiat", engine="1.0", fuel="Gas") #INVALID