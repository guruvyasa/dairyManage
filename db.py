import sqlite3

def createToolbar():
    try:
        q= '''
            create table category(
            id integer primary key,name varchar(10) not null
            )'''
        
        conn= sqlite3.connect('dairy.db')
        conn.execute(q)
        conn.commit()

        q='''
           create table animal (id integer primary key,
           code varchar(10) not null,
           category_id integer not null,
           foreign key(category_id) references category(id)) '''
        
        conn.execute(q)
        conn.commit()
        
        # q='''
        #     create table production (date varchar(10) primary key,
        #     animal_id integer not null,
        #     qty float not null,
        #     foreign key(animal_id) references animal(id))'''

        # conn.execute(q)
        # conn.commit()
        # conn.close()
        # print('table created')
    
    except Exception as e:
        print(e)

def addCategory(name):
    conn= sqlite3.connect('dairy.db')
    try:
        q='''
        insert into category(name)
        values(?)'''
        conn.execute(q,(name,))
        conn.commit()
        return "category created!!"
        # print('category inserted')
    
    except Exception as e:
        print(e)
        return "failure!!"

    finally:
        conn.close()

def getCategories():
    conn= sqlite3.connect('dairy.db')
    try:
        q='''
        select * from category'''
        cur= conn.execute(q)
        categories= cur.fetchall()
        
        return categories
    
    finally:
        conn.close()


def addAnimal(code,cid):
    conn= sqlite3.connect('dairy.db')
    try:
        q='''
        insert into animal(code,category_id)
        values(?,?)'''
        conn.execute(q,(code,cid,))
        conn.commit()
        # print('animal inserted')
        return "animal created!!"    
    except Exception as e:
        print(e)
        return e

    finally:
        conn.close()

def getAnimals():
    conn= sqlite3.connect('dairy.db')
    try:
        q='''
        select animal.id as id,code,category.name from 
        animal inner join category on animal.category_id=category.id
        '''
        cur= conn.execute(q)
        animals= cur.fetchall()
        
        return animals
    except Exception as e:
        print(e)
        return []
    finally:
        conn.close()




if __name__=='__main__':
    createToolbar()
    addCategory('cow')
    addCategory('goat')
    print(getCategories())
    addAnimal('221',1)
    addAnimal('335',2)
    addAnimal('350',1)
    print(getAnimals())
    # addProduction('1/6/23','221',10)
    # addProduction('1/6/23','335',15)
    # addProduction('1/6/23','350',20)
    # print(getProduction())
