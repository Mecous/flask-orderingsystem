from flask_sqlalchemy import SQLAlchemy
#输入密码加密状态
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()
#用户账户登录表
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(50),primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phonenum = db.Column(db.String(50),unique=True)
    addr = db.Column(db.String(50),nullable=False)
    sellers=db.relationship("Order",back_populates="store")


    def __init__(self, id, email, name, password): # 类似与java中的构造器
        self.id = id
        self.email = email
        self.name = name
        self.password = self.set_password(password)

    def set_password(self, password): # 对明文密码进行加密，返回的是加密后的密码
        return generate_password_hash(password)

    def check_password(self, password): # 检查密码，传入的是明文密码，会将明文密码进行加密后再进行比对
        return check_password_hash(self.password, password)

    def change_password(self, password): # 修改密码
        self.password = self.set_password(password)
    def __repr__(self):
        return '<User: {}, {}>'.format(self.password_hash, self.email)

#商家账户登录表
class Seller(db.Model):
    __tablename__="sellers"
    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phonenum = db.Column(db.String(50),unique=True)
    addr = db.Column(db.String(50),nullable=False)
    users = db.relationship("Order",back_populates="customs")
    menu = db.relationship('Menu',back_populates='store',lazy='dynamic')
    
    def __init__(self, id, email, name, password):
        self.id = id
        self.email = email
        self.name = name
        self.password = self.set_password(password)

    def set_password(self, password): 
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def change_password(self, password):
        self.password = self.set_password(password)
    def __repr__(self):
        return '<Seller: {}, {}>'.format(self.password_hash, self.email)
#菜单表
class Menu(db.Model):
    __tablename__="menu"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    store_id = db.Column(db.String(50),db.ForeignKey("sellers.id"))
    price = db.Column(db.Float(30))
    store = db.relationship("Seller",back_populates="menu")
 
    def __init__(self,id ,name, store_id, price):
        self.id = id
        self.name = name
        self.store_id = store_id
        self.price = price
#订单表
class Order(db.Model):
    __tablename__="orders"
    order_id = db.Column(db.String(50),primary_key = True)
    seller_id = db.Column(db.String(50),db.ForeignKey("sellers.id"),primary_key=True)#商家代号做为外键带入订单号里
    user_id = db.Column(db.String(50),db.ForeignKey("users.id"),primary_key=True)#用户代号作为外键带入订单中
    order_date = db.Column(db.Date,nullable = False)
    total_price = db.Column(db.Float(20),nullable = False)
    store = db.relationship("Seller",back_populates="users")
    custom = db.relationship("User",back_populates="sellers")

#变量初始化
    def __init__(self,order_id,seller_id,user_id,order_date):
        self.order_id = order_id
        self.seller_id = seller_id
        self.user_id = user_id
        self.order_date = order_date


