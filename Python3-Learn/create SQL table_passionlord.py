import  pymysql as ps

try:
    cn = ps.connect(host='localhost',port=3306,user='root',password='123',db='tata')
    '''
    cursor() is used to create command
    object, which is use to supply sql queries
    to database engine
    '''
    cmd = cn.cursor()
    query = "create table products(productid varchar(10) primary key,productname varchar(45),productrate decimal(10),mfdate date)"
    cmd.execute(query)
    print("Table Created..")
    cn.commit()
    cn.close()
except Exception as e:
    print("Error:",e)
