from app import app
from models import db, Cupcake

db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="vanilla",
    size="medium",
    rating=4,
    image="https://assets.epicurious.com/photos/57d6d471adcedbfa6105f654/5:4/w_830,h_663,c_limit/amy-sedariss-vanilla-cupcakes.jpg"
)

c4 = Cupcake(
    flavor="birthday cake",
    size="small",
    rating=7,
    image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxTITameRWQJ6wHwx7yiguO5Zs20uvXDiH3w&usqp=CAU"
)

c5 = Cupcake(
    flavor="butterscotch",
    size="large",
    rating=10,
)

db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()