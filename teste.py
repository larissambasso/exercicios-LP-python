from fastapi import FastAPI

encontrando = FastAPI()

vendas = {
  1:{"item": "lata","preço unitário":4,"quantidade":5},
  2:{"item": "lata","preço unitário":15,"quantidade":5},
  3:{"item": "lata","preço unitário":10,"quantidade":5},
  4:{"item": "lata","preço unitário":2,"quantidade":5},
}


@encontrando.get("/")
def home():
  return {"Vendas":len(vendas)}

@encontrando.get("/vendas")
def todas_vendas():
  return vendas

@encontrando.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
  if id_venda in vendas:
    return vendas[id_venda]
  else:
    return{"Erro":"ID Venda inexistente"}
