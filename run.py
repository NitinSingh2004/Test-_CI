import uvicorn
from fastapi import FastAPI
app=FastAPI()

class Item:
    a:int
    b:int

@app.post("/test")
def test(item:Item):
    a=item.a
    b=item.b
    c=a+b
    return {"message":f"The sum of {a} and {b} is {c}"}

if __name__=="__main__":   
    uvicorn.run(app,host="0.0.0.0",port=8000)
