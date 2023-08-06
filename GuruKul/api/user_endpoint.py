from starlette.responses import JSONResponse
from sqlalchemy import select

from database.model.user_model import User
from utilities.tokennizer import encode, decode
from database.schema.user_schema import (UserBase, UserCreate, 
                                         UserLogin, UserDetail)
from database.database_config import session_local_manager, async_engine
from sqlalchemy.sql import text

import bcrypt
import base64

async def user_register(request):
    """
    This function creates the new user
    """
    data = await request.json()
    # print("data got from client :", data)
    hashed_password = bcrypt.hashpw(
                        data['password'].encode("utf-8"),
                        bcrypt.gensalt())
    print(data)
    print("hashed_pass", hashed_password)
  
    # email = data['email']
    # async with async_engine.connect() as connection:
    #     query = text("select email, password from users where email = :email")
    #     result = await connection.execute(query.bindparams(email=email))
    #     user = result.fetchone()
    #     print({"email":user.email})


    with session_local_manager() as db:
        # db = session_local()
        user = db.query(User).filter(User.email == data['email']).first()
        if user:
            return JSONResponse({
                "message":"User Already Registered"
            })
        new_user = User(
            email=data['email'],
            role=data['role'],
            username=data['username'],
        )
        new_user.password = hashed_password
        db.add(new_user)
      
    return JSONResponse({
        "message":"Successfully logged in"
    })


async def user_login(request):
    data = await request.json()
    print("In ",data)


    # hashed_password = bcrypt.hashpw(
    #                     data['password'].encode("utf-8"),
    #                     bcrypt.gensalt())
    # print("Before :",hashed_password)
    # print("Hashed password :",base64.b64encode(hashed_password).decode())

    with session_local_manager() as db:
        # db = session_local()
        user = db.query(User).filter(User.email == data['email']).first()

        # print("User is ",user.password)
        if not user:
            return JSONResponse({
                "msg":"User not registered"
            })
        else:
            if bcrypt.checkpw(data.get('password').encode('utf-8'),user.password):
                token = encode(
                    user_id=user.id,
                    username=user.username
                )
                return JSONResponse({
                    "title": "user_login",
                    "message": "User logged in successfully",
                    "data":{
                        "user_id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "token": token
                    },
                    },
                    status_code=200)


    return JSONResponse({
        "msg":"Got into"
    })






        # hashed_password = bcrypt.hashpw(
        #                 data['password'].encode("utf-8"),
        #                 bcrypt.gensalt())
        
        # print("hashed password is :",hashed_password)
              
        # return JSONResponse({
        #     "passowed":data['password'],
        #     "hash_password": str(user.password)
            
        # })




    #     if not user:
    #         return JSONResponse({
    #             "message":"User Not Registered"
    #         })
    #     else:
    #         print("Hashed password from gen",base64.b64encode(hashed_password).decode())
    #         print("Users hash password", user.password)

#     """
#     It logs the user into our system
#     """
#     data = await request.json()
#     print("Data for login:", data)

#     with session_local_manager() as db:  # Use a context manager to manage the database session
#         user = db.query(User).filter(User.email == data['email']).first()
#         if not user:
#             return JSONResponse({"message": "User with that email not found"})

#         else:
#             return JSONResponse({
#                 "message": "Incorrect password"
#             })