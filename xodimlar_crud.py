# CRUD - create, read, update, delete 
# create - insert , read - select * from , update - update , delete - delete from 


# create - internetga ma'lumot  qo'shish 
# read - ma'lumotni internetdan olish ( o'qish )
# update - qachonlardir internetda ma'lumotingizni create qilgan bo'lsangiz va uni o'zgartirmoqchi bo'lsangiz 
# delete -internetdagi ma'lumotlaringizni o'chirib tashlash 

from db import get_connection

conn = get_connection


# C R E A T E - I N S E R T 
 # bitta ma'lumot qoshish 
def xodim_qosh(conn, ism, maosh, bolim_id):
    with conn.cursor() as cur:
        cur.execute(
            '''
            INSERT INTO xodimlar (ism, maosh, bolim_id)
            VALUES (%s, %s, %s)
            ''',
            ('Ali', 100000000, 'IT bolimi')
        )
    conn.commit()
    print(f'{ism} muvaffaqiyatli qo\'shildi!')

xodim_qosh(conn, 'Zafar', 7500000, 1)

# returning id - id sini qaytarish 
def xodim_qosh_id_bilan(conn, ism, maosh):
    with conn.cursor() as cur:
        cur.execute(
            '''
            INSERT INTO xodimlar (ism, maosh)
            VALUES (%s, %s)
            RETURNING id
            ''',
            (ism, maosh)
        )
        yangi_id = cur.fetchone()[0]
    conn.commit()
    return yangi_id

id = xodim_qosh_id_bilan(conn, 'Nodira', 8000000)
print(f'Yangi ID: {id}')


# #def asfdg(d,fh):

    
#     print()


# a = asfdg(12, 'asdfdgh')


# bir nechta ma'lumotni birdaniga qo'shish 
yangi_xodimlar = [
    ('Alisher', 8500000, 1),
    ('Malika',  6200000, 2),
    ('Jasur',   9100000, 1),
]

with conn.cursor() as cur:
    cur.executemany(
        'INSERT INTO xodimlar (ism, maosh, bolim_id) VALUES (%s,%s,%s)',
        yangi_xodimlar
    )
conn.commit()
print(f'{len(yangi_xodimlar)} ta xodim qo\'shildi!')

# Shularni hammasi postgresqldagi insert ga teng 



#  U P D A T E

# maosh ni id bo'yicha qidirib yangilagan 
def maosh_yangilash(conn, xodim_id, yangi_maosh):
    with conn.cursor() as cur:
        cur.execute(
            'UPDATE xodimlar SET maosh = %s WHERE id = %s',
            (yangi_maosh, xodim_id)
        )
        tasirlangan = cur.rowcount  # nechta qator o'zgardi
    conn.commit()
    print(f'{tasirlangan} ta qator yangilandi')

maosh_yangilash(conn, 3, 9500000)



# rowcount qanday ishlaydi 
cur.execute(
    'UPDATE xodimlar SET maosh = maosh * 1.10 WHERE bolim_id = %s',
    (1,)  # IT bo'limiga 10% ustama
)

print(f'Ozgaritirilgan qatorlar: {cur.rowcount}')
# rowcount = 0 bo'lsa — hech narsa o'zgarmadi
# rowcount = 3 bo'lsa — 3 ta qator yangilandi

conn.commit()


# returning bilan yangilangan qiymatlarni olish 

with conn.cursor() as cur:
    cur.execute(
        '''
        UPDATE xodimlar
        SET maosh = maosh + %s
        WHERE id = %s
        RETURNING id, ism, maosh
        ''',
        (500000, 2)
    )
    yangilangan = cur.fetchone()
    print(f'Yangi maosh: {yangilangan[2]:,}')
conn.commit()



